# coding: utf-8 2018/9/6 13:49

from setuptools import setup, find_packages

setup(
    name="qycli",
    version="0.12",
    packages=find_packages(),
    description="qycli command line",
    long_description="qycli command line",
    author="lijun",
    author_email="naralv@126.com",
    license="MIT",
    url="http://blog.csdn.net/naralv/",
    install_requires=[
        "requests",
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'qycli = qycli.main:main',
        ]
    }
)
