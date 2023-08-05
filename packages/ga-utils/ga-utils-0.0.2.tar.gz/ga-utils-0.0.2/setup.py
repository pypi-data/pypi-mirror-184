#!/usr/bin/env python
#-*- coding:utf-8 -*-
import setuptools

setuptools.setup(
    name="ga-utils",                 
    version="0.0.2",                               
    author="janeluck",  
    license='MIT',
    author_email="janeluck158@outlook.com",
    url="https://git.woa.com/janeajian/ga-util",
    description="通过GA协议获取数据，用于调试GA控件树",
    long_description="通过GA协议获取数据，用于调试GA控件树，示例：ga-utils get 300 --port 2004",
    install_requires=[
    'xmltodict>=0.13.0'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points = {
        'console_scripts': [
            'ga-utils=ga_utils.main:main',
        ]
    }
)