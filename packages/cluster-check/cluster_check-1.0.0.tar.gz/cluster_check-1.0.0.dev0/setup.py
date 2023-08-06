#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='cluster_check',
    version='1.0.0.dev',
    url='https://github.com/huozhihui/cluster_check',
    license='BSD',
    author='Huozhihui',
    author_email='240516816@qq.com',
    description='Xtao storage cluster check.',
    long_description='',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # packages=find_packages(exclude=('doc*',), include=('ansible*', 'other*', 'scripts*',)),
    # install_requires=[  # 安装依赖的其他包
    #     'docutils>=0.3',
    #     'requests',
    # ],
    # 设置程序的入口为hello
    # 安装后，命令行执行hello相当于调用hello.py中的main方法
    entry_points={
        'console_scripts': [
            'cluster_check = cluster_check.scripts.xj:main'
        ]
    },
    zip_safe=False,
    platforms='any'
)
