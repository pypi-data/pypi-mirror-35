# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 下午2:03
# @Author  : Mori
# @Email   : moridisa@moridisa.cn
# @File    : net_works.py

import re
import json
import logging
import telnetlib
from typing import Iterable, Dict, Tuple
from .data_operator import get_zookeeper_host
from kazoo.client import KazooClient

__all__ = [
    'set_dubbo_decode',
    'format_return_data',
    'invoke_dubbo',
    'DubboParamInstance'
]

brackets_match = re.compile('\(|\)')
__decode_fmt__ = 'gbk'


def set_dubbo_decode(decode: str):
    """
    set decode format

    :param decode: decode name
    """
    global __decode_fmt__
    __decode_fmt__ = decode


def format_return_data(data: Iterable, count: int = None, msg: str = None, status: bool = True) -> Dict:
    """
    format response message for http

    :param data: data
    :param count: len of data
    :param msg: message
    :param status: success / fail
    """
    data = {
        'count': len(list(data)),
        'status': 'Success' if status is True else 'Fail',
        'data': data
    }
    if count:
        data['count'] = count
    if msg:
        data['msg'] = msg
    return data


def __write_to_dubbo(tn: telnetlib.Telnet, cmd: str):
    """
    write command to dubbo by telnet client

    :param tn: telnet client
    :param cmd: command
    """
    decode_cmd = cmd.encode(__decode_fmt__)
    decode_cmd += b'\n'

    logging.info(decode_cmd)
    tn.write(decode_cmd)


def __read_from_dubbo(tn: telnetlib.Telnet) -> str:
    """
    read feedback from dubbo telnet

    :param tn: telnet client
    :return: content
    """
    total_content = tn.read_until('dubbo>'.encode(__decode_fmt__), 2).decode(__decode_fmt__)
    total_content = total_content.split('dubbo>')[0]
    return total_content.split('elapsed:')[0]


def __read_dubbo_host_port(service: str, config_name: str) -> Tuple[str, str]:
    """
    从zookeeper 获取 dubbo地址和端口 --- author: Tatum (塔叔❤️)

    read host and prot for dubbo from zookeeper --- author: Tatum (塔叔❤️)

    :param service: 服务名
    :param config_name: 配置名
    :return: 地址, 端口
    """
    zk = KazooClient(hosts=get_zookeeper_host(config_name))
    zk.start()
    providers_node = '/dubbo/{0}/providers'.format(service)
    providers = zk.get_children(providers_node)
    zk.stop()
    zk.close()
    if len(providers) == 0:
        raise Exception('None service found')
    provider = providers[0]
    m = re.match(r'dubbo%3A%2F%2F(?P<host>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})%3A(?P<port>[0-9]{1,5})%2F.*',
                 provider)
    return m.group('host'), m.group('port')


class DubboParamInstance:
    """
    dubbo parameter instance
    """

    def __init__(self, class_name: str, **kwargs):
        """
        create a instance for dubbo api instance param

        :param class_name: class name of parameter
        :param kwargs: data
        """
        self.param = {'class': class_name}
        for k in kwargs:
            if isinstance(kwargs[k], dict):
                kwargs[k] = json.dumps(kwargs[k])
            elif isinstance(kwargs[k], list):
                kwargs[k] = json.dumps(kwargs[k])
        self.param.update(kwargs)

    def __str__(self):
        return json.dumps(self.param)

    def __repr__(self):
        return self.__str__()


def invoke_dubbo(service: str, method: str, config_name: str, args: Iterable, decode_charset='gbk'):
    """
    call dubbo api

    调用dubbo 接口

    :param service: service name
    :param method: method name
    :param config_name: config in yaml for zookeeper
    :param decode_charset: gbk
    :param args: data
    :return: result
    """
    # telnet connect to dubbo service
    host, port = __read_dubbo_host_port(service, config_name)
    tn = telnetlib.Telnet(host=host, port=int(port))

    # send command line
    __write_to_dubbo(tn, f'ls -l {service}')

    # read from telnet
    content = __read_from_dubbo(tn)
    target_method_info = next(filter(lambda x: ' ' + method + '(' in x, content.split('\r\n')))
    pure_args_for_method = re.sub(r'\(|\)', '', target_method_info.split(method)[1]).split(',')

    default_args = []
    args_string_indexs = []
    for index, i in enumerate(pure_args_for_method):
        if i == 'java.lang.String':
            default_args.append(''),
            args_string_indexs.append(index)
        elif i == 'int':
            default_args.append(0),
        elif i == 'boolean':
            default_args.append('true')
        elif i == 'double' or i == 'float':
            default_args.append(0.0)
        elif '[]' in i:
            default_args.append([])
        elif i == '':
            default_args.append('')
        else:
            default_args.append('null')

    args = list(args)
    if len(args) != len(default_args):
        raise ValueError(f'Args length is not match expectation: {len(default_args)} parameters')
    for i in range(len(default_args)):
        if args[i] is None:
            args[i] = default_args[i]
        elif isinstance(args[i], bool):
            args[i] = 'true' if args[i] else 'false'

    formated_args = ','.join([f'"{x}"' if args.index(x) in args_string_indexs else str(x) for x in args])
    __write_to_dubbo(tn, f'invoke {service}.{method}({formated_args})')
    result = __read_from_dubbo(tn)
    try:
        return json.loads(result, encoding=decode_charset)
    except Exception as e:
        logging.error(e)
        return result
