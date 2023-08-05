#!/usr/bin/env python
#coding:utf-8

from setuptools import setup

setup(
    name = "lgx",
    version = "1.0.1",
    author = "laoguo",
    author_email = "laoguo@126.com",
    url = "http://www.laoguo.com",
    description = u"are you ok?",
    packages = ["lgx"],
    install_requires = ["numpy"],
    entry_points = {
        'console_scripts' : [
            'lgx_x=lgx:lgx_x',
            'lgx_y=lgx:lgx_y',
        ]
    }
)

