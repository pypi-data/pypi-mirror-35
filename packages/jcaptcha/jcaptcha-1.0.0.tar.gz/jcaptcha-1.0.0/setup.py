#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages, Extension


setup(
    name='jcaptcha',
      version='1.0.0',
      description='验证码生成',
      url='http://github.com/xiaofeng283',
      author='Jervon',
      author_email='xiaofeng283@gmail.com',
      license='MIT',
      # packages = find_packages(),
      packages = ['jcaptcha'],
      include_package_data = True,
      # package_data = {'captcha': ["*.py"], 'fonts': ["SIMYOU.TTF"]},
      package_dir={'jcaptcha': 'jcaptcha',},
      # package_data={'fonts': ['jcaptcha/SIMYOU.TTF']},
      # packages=['jcaptcha',],
      # py_modules=['jcaptcha',],#包中需要可见的模块
      zip_safe=False,
      # ext_modules=[Extension('jcaptcha', ['SIMYOU.TTF'])],
      install_requires = ["captcha"]
)