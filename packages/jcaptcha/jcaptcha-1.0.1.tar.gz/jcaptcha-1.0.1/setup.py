#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages, Extension


setup(
    name='jcaptcha',
      version='1.0.1',
      description='验证码生成',
      url='http://github.com/xiaofeng283',
      author='Jervon',
      author_email='xiaofeng283@gmail.com',
      license='MIT',
      packages = ['jcaptcha'],
      include_package_data = True,
      package_dir={'jcaptcha': 'jcaptcha',},
      zip_safe=False,
      install_requires = [
        "captcha",
        "numpy",
        "matplotlib",
        "Pillow",
        ]
)