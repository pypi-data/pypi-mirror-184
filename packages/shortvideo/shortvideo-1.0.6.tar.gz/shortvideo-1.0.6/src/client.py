import asyncio
import datetime
import os
import re
import math
from typing import Any, Dict, List
import json
import random
from fake_useragent import UserAgent

from .method import Method, Result
from .utils import idle
import requests

version = '1.0.6'


class File:
    def __init__(self, id: int, label: str, md5: str, src: str, size: int, accept: str, name: str, cos: dict = None, **kwargs) -> None:
        self.id = id
        self.label = label
        self.md5 = md5
        self.src = src
        self.size = size
        self.accept = accept
        self.name = name
        self.cos = cos

    @property
    def sizeStr(self):
        value = 0
        unit = ''
        if self.size < 1024:
            value = self.size
            unit = 'B'
        elif self.size < 1024*1024:
            value = self.size/1024
            unit = 'KB'
        elif self.size < 1024*1024*1024:
            value = self.size/1024/1024
            unit = 'MB'
        else:
            value = self.size/1024/1024/1024
            unit = 'GB'
        return f'{math.ceil(value*10)/10}{unit}'


class Client(Method):
    appid: str
    appsecret: str
    host: str
    workdir: str
    index: int
    do_action: str
    mode: str

    def __init__(self):
        self.appid = ''
        self.appsecret = ''
        self.host = ''
        self.workdir = ''
        self.version = version
        self.index = 0
        self.do_action = ''
        self.mode = ''

    async def start(self):
        if not await self.settings():
            await idle(exit=True)
            return

        async def do(value: str):
            self.index = 0
            self.do_action = value
            if value == '2':
                await self.read()
                # await self.cosCopy()
            elif value == '1':
                print('\n\033[31m要中断程序，请同时按下 ctrl+c\033[0m\n')
                await idle(self.read)

        await self.home(do)

    async def ctrl(self, response: Result):
        if response.code == 401:
            print(response.msg)
            await idle(exit=True)
            return
        if(not response.success or not response.data or not isinstance(response.data, dict)):
            print(response.msg or '请求任务时发生未知错误')
            if self.do_action == '2':
                return
            s = 10
            if isinstance(response.data, dict):
                s = response.data.get('seconds') or 10
            if s >= 5:
                await asyncio.sleep(s)
            return

        seconds = response.data.get('seconds')
        if seconds:
            if self.do_action == '2':
                return
            next = datetime.datetime.now()+datetime.timedelta(seconds=seconds)
            print(
                f'\r暂无任务，{seconds}秒后({next.strftime("%H:%M:%S")})将再次读取...', end=' ')
            await asyncio.sleep(seconds)
            return

        return True

    async def read(self):
        kwargs = dict(mode=self.mode)
        if self.mode == 'imitate':
            kwargs['user_agent'] = UserAgent().random
        # kwargs['mode']='webpublish'
        response = await self.query('/read', **kwargs)
        if not await self.ctrl(response):
            return

        self.index += 1
        mode = response.data.get('mode')
        video = response.data.get('video')
        session = response.data.get('session')
        account = response.data.get('account')

        _id = video.get('_id')
        status = video.get('status')
        title = video.get('title')
        record_caption = video.get('name')
        if account:
            record_caption += f'【\033[35m{account.get("name")}.{account.get("weight")}\033[0m】'

        print(f'\n{self.index}){record_caption}')

        # 首先下载视频
        files = [File(**x) for x in video.get('files')]
        result, cosRes = await self.downloadAndUpload(video.get('category_name'), files)

        kwargs = dict(_id=_id, title=title, status=status, mode=mode)

        if len(result) != len(files):
            await self.query('/updateStatus', **kwargs, childStatus='error', error="未能完全下载")
            return

        if mode == 'webupload' or status == 'export':
            res = await self.query('/updateStatus', **kwargs, childStatus='exported', cosRes=cosRes)
            if res.msg:
                print(f'\t{res.msg}')

        elif mode in ['webpublish', 'imitate', 'api']:
            if len(cosRes) != len(files):
                await self.query('/updateStatus', **kwargs, childStatus='error', error="未能完全上传")
                return

            kwargs.update({'childStatus': 'uploaded', 'cosRes': cosRes})

            if mode == 'webpublish':
                res = await self.query('/updateStatus', **kwargs)
                if res.msg:
                    print(f'\r\t{res.msg}')

            elif mode == 'imitate':
                kwargs['session'] = session
                print('\r\t发布中..', end=" ")
                res = await self.query('/updateStatus', **kwargs)
                if res.success:
                    print(f'\r\t\033[32m{res.msg}\033[0m')
                else:
                    print(f'\r\t\033[31m{res.msg}\033[0m')
            elif mode == 'api':
                print('\r\t发布中..', end=" ")
                if video.get('activity'):
                    print('\r\t模拟发布活动', end=" ")
                    res = await self.submit(
                        account.get('mobile'), 
                        account.get('password'), 
                        result[1],
                        video.get('title'), 
                        video.get('category'), 
                        video.get('source'), 
                        video.get('tag'),
                        uploadres_cos=cosRes.get('uploadres_cos'),
                        coverres_cos=cosRes.get('coverres_cos'),
                        coverres2_cos=cosRes.get('coverres2_cos'),
                        coverres1_cos=cosRes.get('coverres1_cos'),
                        activity=video.get('activity')
                    )
                else:
                    # res = await self.query('/updateStatus', **kwargs)
                    res = await self.api_publish(video, account.get('app_id'), account.get('app_token'), cosRes)
                kwargs['childStatus'] = 'completed'
                kwargs.update(res.data)
                await self.query('/updateStatus', **kwargs)
                code = kwargs.get('code')
                message = kwargs.get('message')
                if code == 0:
                    print(f'\r\t\033[32m{message}\033[0m')
                else:
                    print(f'\r\t\033[31m{message}\033[0m')

            else:
                print(f'\t无效的发布方式({mode})')

    async def downloadAndUpload(self, category_name: str, files: List[File]):
        savepath = os.path.join(
            self.workdir, datetime.datetime.now().strftime('%Y%m%d'))
        if not os.path.exists(savepath):
            os.mkdir(savepath)
        if category_name:
            savepath = os.path.join(savepath, category_name)
            if not os.path.exists(savepath):
                os.mkdir(savepath)

        cosRes = {}
        result = {}

        # 先下载files中的文件
        for file in files:
            filepath = os.path.join(savepath, file.name)
            allow_up = False
            if os.path.exists(filepath) and os.path.getsize(filepath) == file.size:
                print("\r\t%s(%s) 下载%d%%" %
                      (file.label, file.sizeStr, 100), end=" ")
                allow_up = True
                result[file.id] = filepath
            else:
                success = await self.download(filepath, file.src, lambda p, s, t: print("\r\t%s(%s) 下载%d%%" % (file.label, file.sizeStr, p), end=" "))
                if success and os.path.getsize(filepath) == file.size:
                    allow_up = True
                    result[file.id] = filepath
                else:
                    print('大小不一致' if success else '失败')
                    os.remove(filepath)
                    break

            if not allow_up:
                continue

            cos = file.cos
            if not cos:
                print('完成')
                continue

            accept = file.accept
            res = await self.to_cos(cos, filepath, accept, lambda p, s, t: print("\r\t%s(%s) 下载完成，上传%d%%" % (file.label, file.sizeStr, p), end=" "))
            if res.success:
                print('完成')
                if file.id == 0:
                    cosRes['uploadres_cos'] = res.data
                elif file.id == 1:
                    cosRes['coverres_cos'] = res.data  # coverres_cos 是横版封面
                elif file.id == 2:
                    cosRes['coverres2_cos'] = res.data  # coverres2_cos 是竖版封面
                elif file.id == 3:
                    cosRes['coverres1_cos'] = res.data  # 好像是分屏封面

            else:
                print(f'失败：{res.msg}')
                break
        return result, cosRes

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

        """ if is_video:
            result['headers'] = {
                'content-type': 'application/xml', 'x-cos-request-id': result['RequestId']}
        else:
            result['headers'] = {
                'content-length': '0', 'etag': result['ETag'], 'x-cos-request-id': result['RequestId']} """
        return result

    async def api_publish(self, video: dict, app_id: str, app_token: str, cosRes: dict):
        title = video.get('title')
        uploadres_cos = cosRes.get('uploadres_cos')
        coverres_cos = cosRes.get('coverres_cos')
        coverres2_cos = cosRes.get('coverres2_cos')
        coverres1_cos = cosRes.get('coverres1_cos')
        data = {
            "app_id": app_id,
            "app_token": app_token,
            "title": title,
            "category": video.get('category'),
            "source": video.get('source'),
            "tag": video.get('tag'),
            "activity": video.get("activity") or "",
            "video_cos": self.__formatCosData(uploadres_cos, True),
            'coverinfo_cos': self.__formatCosData(coverres_cos, False)
        }
        if coverres2_cos:
            data['coverinfo2_cos'] = self.__formatCosData(coverres2_cos, False)

        if coverres1_cos:
            data['coverinfo1_cos'] = self.__formatCosData(coverres1_cos, False)

        headers = {'Content-Type': 'application/json'}
        url = 'https://mp.xiaozhuyouban.com/video/publish'

        response = requests.post(url, data=json.dumps(data), headers=headers)

        if(response.status_code == 200):
            value = response.json()
            code = value.get('code')
            message = value.get('message')
            return Result(code == 0, message, dict(code=code, message=message))
        else:
            message = f'发布请求异常({response.status_code})'
            return Result(False, message, dict(code=-1, message=message))
