# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='openfire-restapi',
    version='0.0.1',
    description=u'A python client for Openfire’s REST API Plugin',
    license="GPL-3",
    author='Sergey Fedotov (seamus-45)',
    author_email='s.fido@gmail.com',
    url='https://github.com/seamus-45/openfire-restapi',
    packages=['ofrestapi'],
    install_requires=[
        'requests==2.12.5'
    ]
)
