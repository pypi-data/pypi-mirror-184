from setuptools import setup

packages = ["src"]

requires = [
    "requests==2.28.1",
    "requests_toolbelt==0.9.1",
    "cos_python_sdk_v5==1.9.21",
    "fake_useragent==1.1.1",
    "qcloud_cos==3.3.6"
]


setup(
    name='shortvideo',  # 包名称
    version='1.0.3',  # 包版本
    description='',  # 包详细描述
    long_description='', 
    author='netfere',  # 作者名称
    author_email='netfere@gmail.com',  # 作者邮箱
    url='',   # 项目官网
    packages=packages,    # 项目需要的包
    python_requires=">=3.7",  # Python版本依赖
    install_requires=requires,  # 第三方库依赖
    entry_points={
        'console_scripts':[
            'shortvideo = src.main:main'
        ]
    },
)