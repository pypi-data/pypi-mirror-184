import asyncio
import configparser
import functools
import json
import logging
import os
import platform
from concurrent.futures.thread import ThreadPoolExecutor
from contextlib import closing
from getpass import getpass
from typing import Any, Callable, List
import sys
import requests
from fake_useragent import UserAgent
from qcloud_cos import CosConfig, CosS3Auth, CosS3Client
from qcloud_cos.cos_exception import CosClientError, CosServiceError
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from .object import Object
from .utils import md5, rdValue

log = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO, stream=sys.stdout)

class Result(Object):
    def __init__(self, success: bool, msg: str, data: Any=None, **kwargs) -> None:
        self.success = success
        self.msg = msg or ''
        self.data = data
        self.code = kwargs.get('code') or 0


async def ainput(prompt: str = "", *, hide: bool = False):
    """Just like the built-in input, but async"""
    with ThreadPoolExecutor(1) as executor:
        func = functools.partial(getpass if hide else input, prompt)
        return await asyncio.get_event_loop().run_in_executor(executor, func)

host_uri = 'https://www.shortvideo.work/api/xiaozhu' #'http://192.168.5.84:8012/api/xiaozhu'

#https://gist.github.com/kazqvaizer/4cebebe5db654a414132809f9f88067b
def multipartify(data, parent_key=None, formatter: callable = None) -> dict:
    if formatter is None:
        def formatter(v): return (None, v)  # Multipart representation of value

    if type(data) is not dict:
        return {parent_key: formatter(data)}

    converted = []

    for key, value in data.items():
        current_key = key if parent_key is None else f"{parent_key}[{key}]"
        if type(value) is dict:
            converted.extend(multipartify(
                value, current_key, formatter).items())
        elif type(value) is list:
            for ind, list_value in enumerate(value):
                iter_key = f"{current_key}[{ind}]"
                converted.extend(multipartify(
                    list_value, iter_key, formatter).items())
        else:
            converted.append((current_key, formatter(value)))

    return dict(converted)

config_path = os.path.join(os.path.dirname(__file__),'config.ini')

mode = {'api':'API发文','imitate':'模拟发文','webupload':'网页上传视频发文','webpublish':'网页直接发文'}

class Method:
    async def query(self, url: str, **kwargs):
        def value_string(data: dict):
            array = []
            for k in sorted(data):
                v = data[k]
                if isinstance(v, bool):
                    array.append(f'{k}={str(v).lower()}')
                elif isinstance(v, dict):
                    array.append(f'{k}={value_string(v)}')
                elif(isinstance(v, list)):
                    for i in v:
                        array.append(f'{k}=[{value_string(i)}]')
                else:
                    array.append(f'{k}={v}')
            return '&'.join(array)

        try:
            nonce = rdValue(10)
            data = value_string(kwargs)
            sign = md5(f'{url}{data}{nonce}', self.appsecret)
            
            url = f'{self.host}{url}?appid={self.appid}&nonce={nonce}&sign={sign}&version={self.version}'
            
            headers = {'Content-Type': 'application/json'}
            
            response = requests.post(url, data=json.dumps(
                kwargs), headers=headers) if kwargs else requests.get(url, headers=headers)

            if(response.status_code == 200):
                value = response.json()
                res = Result(value.get('success'),
                             value.get('msg'), value.get('data'))
                if(value.get('code') == 401):
                    res.code = 401
                return res
            else:
                return Result(False, str(response.status_code), None, code=response.status_code)

        except Exception as e:
            return Result(False, str(e), None)

    async def settings(self):
        
        config = configparser.ConfigParser()
        if not os.path.exists(config_path):
            config.add_section("settings")
            config.set("settings", "desc", "请不在擅自修改配置文件，以免引发异常！")
            config.set("settings", "version", self.version)
            config.set("settings", "host", host_uri)
            config.set("settings","mode","api") #'webupload' | 'webpublish' | 'api' | 'imitate'

            config.write(open(config_path, "w"))

        config.read(config_path)

        def get(name: str, default: Any = ''):
            return config.get('settings', name, fallback=default)

        def set(name: str, value: Any):
            config.set('settings', name, value)

        if(get('version') != self.version):
            set('version', self.version)
            config.write(open(config_path, "w"))

        if not get('host'):
            set('host', host_uri)
            config.write(open(config_path, "w"))

        self.host = get('host')
        self.mode = get('mode')

        while(not self.appid or not self.appsecret or not self.workdir):
            is_save = False
            self.appid = get('appid')
            if not self.appid:
                appid = await ainput("请输入AppID：")
                if appid == 'exit':
                    break
                elif not appid:
                    continue
                else:
                    self.appid = appid
                    set('appid', self.appid)
                    is_save = True

            self.appsecret = get('appsecret')
            if not self.appsecret:
                appsecret = await ainput("请输入AppSecret：")
                if appsecret == 'exit':
                    break
                elif not appsecret:
                    continue
                else:
                    self.appsecret = appsecret
                    set('appsecret', self.appsecret)
                    is_save = True

            self.workdir = get('workdir')
            if not self.workdir:
                workdir = await ainput("请输入工作目录：")
                if workdir == 'exit':
                    break
                elif not workdir:
                    continue
                else:
                    if os.path.exists(workdir):
                        self.workdir = workdir
                        set('workdir', self.workdir)
                        is_save = True
                    else:
                        print(f'不存在的目录：{workdir}')
                        continue

            if is_save:
                res = await self.query('/checkSecret', secret=md5(self.appsecret))
                if res.success:
                    config.write(open(config_path, "w"))
                else:
                    print(res.msg)

            break

        return bool(self.appid and self.appsecret and self.workdir)

    async def home(self, callback: Callable[[str], None]):
        def render():
            sysstr = platform.system()
            os.system('cls' if sysstr == 'Windows' else 'clear')
            options = [
                f'\033[31;42m{" "*10}短视频工作平台之客户端({self.version}){" "*10}\033[0m',
                f'{" "*10}www.shortvideo.work\n',f'配置路径：{config_path}\n发文模式：{mode.get(self.mode) or self.mode}\n',
                '1 开始执行任务\t2 只执行一次任务',
                '3 修改AppSecret',
                f'4 修改服务器地址（{self.host}）',
                f'5 修改工作目录（{self.workdir}）',
                '0 退出程序',
                '\n请选择相应操作的序号：'
            ]
            return '\n'.join(options)

        async def setWorkdir():
            workdir = None
            while not workdir:
                workdir = await ainput('请输入新的工作目录（输入0则返回）：')
                if workdir == '0' or workdir == self.workdir:
                    await main()
                elif workdir:
                    if os.path.exists(workdir):
                        config = configparser.ConfigParser()
                        config.read(config_path)
                        config.set('settings', 'workdir', workdir)
                        config.write(open(config_path, "w"))
                        self.workdir = workdir
                        await main()
                    else:
                        print(f'{workdir} 无效')
                        workdir = None
                else:
                    continue

        async def setSecret():
            appsecret = None
            while not appsecret:
                appsecret = await ainput('请输入新的AppSecret（0则返回）：')
                if appsecret == '0':
                    await main()
                elif not appsecret:
                    continue
                else:
                    res = await self.query('/checkSecret', secret=md5(appsecret))
                    if res.success:
                        config = configparser.ConfigParser()
                        config.read(config_path)
                        config.set('settings', 'appsecret', appsecret)
                        config.write(open(config_path, "w"))
                        self.appsecret = appsecret
                        await main()
                    else:
                        print(res.msg)
                        appsecret = None

        async def setHost():
            host = None
            while not host:
                host = await ainput('请输入服务器地址（0则返回）：')
                if host == '0' or host == self.host:
                    await main()
                elif not host:
                    continue
                else:
                    oldHost = self.host
                    self.host = host
                    res = await self.query('/checkSecret', secret=md5(self.appsecret))
                    if res.success:
                        config = configparser.ConfigParser()
                        config.read(config_path)
                        config.set('settings', 'host', self.host)
                        config.write(open(config_path, "w"))
                        await main()
                    else:
                        self.host = oldHost
                        print(res.msg)
                        host = None

        async def main():
            value = None
            while value not in ['0','1', '2', '3', '4', '5']:
                value = await ainput(render())

            if value == '1' or value == '2':
                try:
                    await callback(value)
                except Exception as e:
                    log.error(e,exc_info=True)

            elif value == '3':
                await setSecret()
            elif value == '4':
                await setHost()
            elif value == '5':
                await setWorkdir()
            elif value == '0':
                pass

        await main()

    async def download(self, savepath: str, src: str, callback: Callable[[int, int, int], None]):
        try:
            with closing(requests.get(src, stream=True)) as response:
                chunk_size = 1024  # 单次请求最大值
                total = int(response.headers['content-length'])  # 内容体总大小
                size = 0
                with open(savepath, "wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size = size + len(data)
                        progress = (size / total) * 100
                        callback(progress, size, total)
        except:
            return False
        else:
            return True

    async def to_cos(self, cos: dict, filepath: str, accept: str, callback):
        def cb(monitor):
            progress = (monitor.bytes_read / monitor.len) * 100
            callback(progress, monitor.bytes_read, monitor.len)

        bucket = cos.get('bucket')
        key = cos.get('filekey')
        region = cos.get('region')
        StartTime = cos.get('startTime')
        expiredTime = cos.get('expiredTime')
        credentials = cos.get('credentials') or []
        secret_id = credentials.get('tmpSecretId')
        secret_key = credentials.get('tmpSecretKey')
        token = credentials.get('sessionToken')
        url = f'https://{bucket}.cos.ap-shanghai.myqcloud.com{key}'

        config = CosConfig(Region=region, SecretId=secret_id,
                           SecretKey=secret_key, Token=token)
        client = CosS3Client(config)

        def cb(monitor):
            progress = (monitor.bytes_read / monitor.len) * 100
            callback(progress, monitor.bytes_read, monitor.len)

        fields = {
            'key': key,
            'Content-Type': accept,
            'file': (key, open(filepath, 'rb'), accept)
        }
        e = MultipartEncoder(fields)
        m = MultipartEncoderMonitor(e, cb)
        headers = {
            'Host': f'{bucket}.cos.ap-shanghai.myqcloud.com',
            'Content-Type': m.content_type,
            'x-cos-security-token': token
        }
        headers['Authorization'] = client.get_auth(
            "POST", bucket, key, Expired=expiredTime-StartTime)

        try:
            r = requests.post(url, data=m, headers=headers)

            if(r.status_code == 200 or r.status_code == 204):
                return Result(
                    True, "",
                    {'ETag': r.headers.get('ETag').replace('"', ''), 'Location': r.headers.get(
                        'Location'), 'x-cos-request-id': r.headers.get('x-cos-request-id')}
                )
            else:
                return Result(False, r.text, None)
        except Exception as ex:
            log.error(ex, exc_info=True)
            return Result(False, str(ex), ex)

    async def login(self, mobile: str, password):
        user_agent = UserAgent().random

        url = "https://mp.xiaozhuyouban.com/signin"

        r = requests.get("https://mp.xiaozhuyouban.com/")

        xsrfToken = r.cookies.get("XSRF-TOKEN")

        headers = {
            'authority': 'mp.xiaozhuyouban.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://mp.xiaozhuyouban.com',
            'referer': 'https://mp.xiaozhuyouban.com/',
            'user-agent': user_agent,
            'x-requested-with': 'XMLHttpRequest'
        }
        r = requests.post(
            url,
            data={"xsrfToken": xsrfToken,
                  "mobile": mobile, "password": password,"agree":"on"},
            cookies=r.cookies,
            headers=headers
        )
        if r.status_code == 200:
            data = r.json() or {'code':-1}
            code = data.get('code')
            message = data.get('message') or '登录未知错误'
            if code == 0:
                r.cookies.set('__root_domain_v','.xiaozhuyouban.com')
                return Result(True, '', (user_agent, r.cookies))
            else:
                action = 0
                if '爬虫' in message:
                    action = 401 #全部停止
                return Result(False, message, None,code=action)
        else:
            return Result(False, f'登录失败：{r.status_code}', None)

    def __formatCosData(self, data: dict, is_video: bool):
        result = {'statusCode': 200}
        for key, value in data.items():
            if key == 'Location':
                Location: str = value.replace(
                    'http://', '').replace('https://', '')
                result['Location'] = Location
                if is_video:
                    arr = Location.split('.')
                    result['Bucket'] = arr[0]
                    result['Key'] = '/'.join(Location.split('/')[1:])
            elif key == 'ETag':
                result['ETag'] = f'"{value}"'
            elif key == 'x-cos-request-id':
                result['RequestId'] = value
            elif key == 'UploadId':
                result['UploadId'] = value

        if is_video:
            result['headers'] = {
                'content-type': 'application/xml', 'x-cos-request-id': result['RequestId']}
        else:
            result['headers'] = {
                'content-length': '0', 'etag': result['ETag'], 'x-cos-request-id': result['RequestId']}
        return result

    async def submit(self,
                     mobile: str, password: str,
                     filepath: str,
                     title: str, category: str, source: int, tag: List[str],
                     uploadres_cos: dict,
                     coverres_cos: dict,
                     coverres2_cos: dict = None,
                     coverres1_cos: dict = None,
                     inspiration_cateid: str = None,
                     activity: str = None,
                     desc: str = None
                     ):

        res = await self.login(mobile, password)
        if not res.success:
            return Result(False, res.msg,dict(code=-1,message=res.msg))

        user_agent, cookies = res.data

        xsrfToken = cookies.get('XSRF-TOKEN')

        headers = {
            'authority': 'mp.xiaozhuyouban.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'origin': 'https://mp.xiaozhuyouban.com',
            'referer': 'https://mp.xiaozhuyouban.com/content/publish',
            'user-agent': user_agent,
            'x-requested-with': 'XMLHttpRequest',
            'x-csrf-token': xsrfToken,
        }

        payload = {
            'title': title,
            'cover': 0,
            'category': category,
            'source': source,
            'tag': tag,
            'inspiration_cateid': inspiration_cateid or '',
            'activity': activity or '',
            'desc': desc or '',
            'video_cos': self.__formatCosData(uploadres_cos, True),
            'coverinfo_cos': self.__formatCosData(coverres_cos, False)
        }
        if coverres2_cos:
            payload['coverinfo2_cos'] = self.__formatCosData(
                coverres2_cos, False)
        if coverres1_cos:
            payload['coverinfo1_cos'] = self.__formatCosData(
                coverres1_cos, False)

        value = multipartify(payload)
        value["coverfile"] = (f'{title}.jpg', open(filepath, 'rb'), 'image/jpeg')
        
        r = requests.post(
            'https://mp.xiaozhuyouban.com/content/publish',
            files=value, headers=headers, cookies=cookies
        )
        
        if r.status_code == 200:
            data = r.json() or {'code':-1}
            code = data.get('code')
            message = data.get('message') or '发布未知错误'
            return Result(code == 0, message,dict(code=code, message=message))
            if code == 0:
                return Result(True, message,dict(code=code, message=message))
            else:
                action = 0
                if '爬虫' in message or message == '周六，周日限制发文':
                    action = 401 #全部停止
                return Result(False, message,code=action)
        else:
            message = f'请求出错：{r.status_code}'
            return Result(False, message,dict(code=-1,message=message))

