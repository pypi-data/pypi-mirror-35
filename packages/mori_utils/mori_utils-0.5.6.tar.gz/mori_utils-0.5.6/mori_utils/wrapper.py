# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/24 上午11:14
# @Author  : Mori
# @Email   : moridisa@moridisa.cn
# @File    : __init__.py.py

import os
import time
import pickle
import logging
import hashlib
from typing import List
from . import CACHE_PATH
from functools import wraps

logger = logging.getLogger('mori_utils')

__all__ = ['m_wrap']


def m_wrap(log: bool = True,
           cache: bool = True,
           cache_expire: float = None,
           prefix: str = None,
           suffix: str = None,
           cache_args: List[int] = None,
           cache_kwargs: List[str] = None,
           cache_args_enable: bool = True):
    def wrapper(func):
        @wraps(func)
        def __inner_wrapper__(*args, **kwargs):
            if log:
                logger.info(f'{func.__module__}.{func.__name__} - Start')

            if cache:
                cache_file_name = f'{func.__module__}.{func.__name__}'
                if prefix:
                    cache_file_name = prefix + '_' + cache_file_name
                if suffix:
                    cache_file_name = cache_file_name + '_' + suffix
                cache_file_name = os.path.join(CACHE_PATH, cache_file_name)

                # check args & kwargs
                if len(args) > 0 or len(kwargs) > 0 and cache_args_enable:
                    if cache_args is not None and (len(cache_args) > 0 or len(cache_kwargs) > 0):
                        if cache_args:
                            been_cache_args = list(map(args.__getitem__,
                                                       filter(lambda x: x < len(args), cache_args)))
                        else:
                            been_cache_args = []
                        if cache_kwargs:
                            been_cache_kwargs = list(map(kwargs.__getitem__,
                                                         filter(lambda x: x in kwargs, cache_kwargs)))
                        else:
                            been_cache_kwargs = []
                    else:
                        been_cache_args = args
                        been_cache_kwargs = kwargs
                    md5 = hashlib.md5()
                    md5.update(f'{been_cache_args}-{been_cache_kwargs}'.encode('utf8'))
                    cache_file_name = f'{cache_file_name}.{md5.hexdigest()[8:-8]}'
                # update cache file name

                cache_file_name = f'{cache_file_name}.cache'

                # check cache file exists
                if os.path.exists(cache_file_name):

                    # cache still work
                    if cache_expire is None or \
                            time.time() - os.path.getmtime(cache_file_name) < cache_expire * 24 * 60 * 60:
                        data = pickle.load(open(cache_file_name, 'rb'))

                    # new cache
                    else:
                        data = func(*args, **kwargs)
                        pickle.dump(data, open(cache_file_name, 'wb'))
                else:
                    data = func(*args, **kwargs)
                    pickle.dump(data, open(cache_file_name, 'wb'))

            else:
                data = func(*args, **kwargs)

            if log:
                logger.info(f'{func.__module__}.{func.__name__} - Finish')
            return data

        return __inner_wrapper__

    return wrapper
