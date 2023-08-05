#coding=utf-8
from distutils.core import setup

setup(
    name="lixia", #对外我们模块的名字
    version="1.0",  #版本号
    description="第一个",  #描述
    author="孙胜杰",   #作者
    author_email="570269783@qq.com",
    py_modules=["one.demo1","one.demo2"]    #要发布的模块，指的是setup.py同级目录的demo1
)