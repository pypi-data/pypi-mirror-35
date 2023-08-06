# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/24 上午11:14
# @Author  : Mori
# @Email   : moridisa@moridisa.cn
# @File    : __init__.py.py

import os

FILE_ROOT = os.getcwd()
LOG_PATH = os.path.join(FILE_ROOT, 'log')
CACHE_PATH = os.path.join(FILE_ROOT, 'caches')
CONFIG_PATH = os.path.join(FILE_ROOT, 'config')
CURRENT_PROJECT_NAME = FILE_ROOT.split(os.path.sep)[-1]

__version__ = (0, 5, 6)
__author__ = "Mori <moridisa@moridisa.cn>"
__status__ = "release"
__date__ = '2018/8/29'
__all__ = []

from .data_operator import *
from .net_works import *
from .exception import *
from .utils import *
from .wrapper import *

try:
    __PATHS__ = [LOG_PATH, CACHE_PATH, CONFIG_PATH]
    [os.mkdir(i) for i in filter(lambda x: os.path.exists(x) is False, __PATHS__)]
    # map(os.mkdir, filter(lambda x: os.path.exists(x) is False, __PATHS__))
    load_config(os.path.join(FILE_ROOT, 'config'))
    logger = gen_logger(f'{__package__}')
    logger.info('mori_utils standby')
except Exception as e:
    print(e)
    print('Mori Utils Load Failed')

__all__ += ['FILE_ROOT', 'LOG_PATH', 'CACHE_PATH', 'CONFIG_PATH']
__all__ += [s for s in dir() if not s.startswith('_')]
