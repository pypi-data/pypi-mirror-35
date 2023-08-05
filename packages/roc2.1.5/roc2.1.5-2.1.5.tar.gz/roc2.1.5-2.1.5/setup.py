# -*- coding: utf-8 -*-

from distutils.core import setup
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here,"README.txt"),"r") as fh:
    long_description=fh.read()

    
setup(

    name = 'roc2.1.5',

    version = '2.1.5',

    keywords = ('simple', 'test'),

    description = 'just a simple test of vipkid',
    
    long_description=long_description,
    
    long_description_content_type="text/markdown",
    charset='UTF-8',
    variant='GFM',

    license = 'MIT',

    author = 'yin',

    author_email = 'yinmengmeng@vipkid.com.cn',

    packages = find_packages(),

    platforms = 'any',

    py_modules=['ROC.drawpic','ROC.roc','ROC.DataOfRoc','ROC.IOU','ROC.scoreRoc','transform.txt2xml','transform.xml2txt','nms.nms']

)

