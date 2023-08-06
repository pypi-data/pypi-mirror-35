#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(
  name='HeliumBot',
  version='0.1.1',
  description='A Discord bot framework in Hy. Supports loading Hy and Python plugins',
  author='Nickolay Ilyushin',
  author_email='nickolay02@inbox.ru',
  url='https://github.com/handicraftsman/heliumbot',
  packages=['heliumbot', 'heliumbot.bot', 'heliumbot.cmd', 'heliumbot.plugins'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Lisp',
    'License :: OSI Approved :: MIT License',
    'Topic :: Communications :: Chat'
  ],
  license='MIT',
  keywords=['discord', 'bot', 'framework', 'hy'],
  install_requires=[
    'discord.py',
    'log4py',
    'redis',
    'hy'
  ],
)