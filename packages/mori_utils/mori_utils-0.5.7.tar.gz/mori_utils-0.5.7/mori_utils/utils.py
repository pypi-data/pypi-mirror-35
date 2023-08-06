# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/24 上午11:14
# @Author  : Mori
# @Email   : moridisa@moridisa.cn
# @File    : __init__.py.py

import os
import sys
import yaml
import smtplib
import logging
from email.header import Header
from email.mime.text import MIMEText
from typing import Dict, List
from . import LOG_PATH, CURRENT_PROJECT_NAME
from .exception import *

__GLOBAL_CONFIGS__ = dict()

__all__ = ['gen_logger', 'read_config', 'load_config', 'arg_check', 'MailHandler']


class MailHandler(logging.Handler):
    """
    Logger Handler to mail err msg
    """

    mail_base = '~~~~~~~~~~~~~~~Congratulation your code FAIL~~~~~~~~~~~~~~~~~~~~\n' \
                '\n' \
                'Please check on path : {path}\n' \
                '              module : {module}\n' \
                '              lineno : {lineno}\n' \
                '            funcName : {funcName}\n' \
                '\n' \
                '\n' \
                'ERR_MSG:\n' \
                '{errmsg}\n' \
                '\n' \
                '~~~~~~~~~~~~~~~~~~~~~~~BTW your code Suck~~~~~~~~~~~~~~~~~~~~~~~\n'

    def __init__(self, mail_config: Dict[str, str]):
        """
        need to define which mail config to use

        :param mail_config: config name
        """
        self.mail_config = mail_config
        super(MailHandler, self).__init__(logging.ERROR)

    def emit(self, record):
        smtp = smtplib.SMTP_SSL(self.mail_config['sender_url'], int(self.mail_config['sender_port']))
        smtp.login(self.mail_config['sender_username'], self.mail_config['sender_password'])
        content = MIMEText(MailHandler.mail_base.format(
            path=record.pathname,
            module=record.module,
            lineno=record.lineno,
            funcName=record.funcName,
            errmsg=record.msg),
            'plain',
            'utf8'
        )
        content['From'] = self.mail_config['sender_username']
        content['To'] = self.mail_config['reciver']
        content['Subject'] = Header(f'Error On {CURRENT_PROJECT_NAME}', 'utf-8')
        smtp.sendmail(self.mail_config['sender_username'], self.mail_config['reciver'].split(';'), content.as_string())


def gen_logger(logger_name: str, mail_config: str = None) -> logging.Logger:
    """
    generator a logger

    :param logger_name: logger name
    :param mail_config: config of e-mail
    :return: logger
    """

    logger = logging.getLogger(logger_name)
    if len(logger.handlers) == 0:
        logger.propagate = False
        logging_format = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', '%Y-%m-%d %H:%M:%S')

        file_log = logging.FileHandler(os.path.join(LOG_PATH, f'{logger_name}.log'))
        console_log = logging.StreamHandler(sys.stdout)

        file_log.setFormatter(logging_format)
        console_log.setFormatter(logging_format)

        logger.setLevel(logging.INFO)

        logger.addHandler(file_log)
        logger.addHandler(console_log)
    if mail_config is not None:
        arg_check(arg_check(mail_config,
                            ['sender_url', 'sender_port', 'sender_username', 'sender_password', 'reciver']))
        logger.addHandler(MailHandler(read_config(mail_config)))
    return logger


def load_config(root_path: str):
    """
    load all config files

    :param root_path: root path
    """

    for file in filter(lambda x: x.endswith('.yaml'), os.listdir(root_path)):
        config = yaml.load(open(os.path.join(root_path, file), 'r'))
        for k in config:
            sub_config = config[k]
            if sub_config.get('need_mysql_extract', None) is not None:
                host = sub_config['host']
                host = host.replace('jdbc:mysql://', '')
                host, db = host.split('/')
                db = db.split('?')[0]
                host, port = host.split(':')
                sub_config.pop('host')
                sub_config['host'] = host
                sub_config['port'] = int(port)
                sub_config['db'] = db
                sub_config.pop('need_mysql_extract')
                config[k] = sub_config
        __GLOBAL_CONFIGS__.update(config)


def arg_check(config_name: str, arg_names: List[str]):
    """
    check is all all args name in config

    :param config_name: config name
    :param arg_names: all args name required
    """

    config = read_config(config_name)
    no_in_args = list(filter(lambda x: x not in config, arg_names))
    if len(no_in_args) != 0:
        raise AttributeNotFound(f'"{";".join(no_in_args)}" Not Found In Config: {config_name}')


def read_config(config_name: str) -> Dict[str, str]:
    """"
    read a config from yaml name

    :param config_name: config dict
    :return:
    """
    if config_name not in __GLOBAL_CONFIGS__:
        raise ConfigNoFound(f'"{config_name}" not found')
    return __GLOBAL_CONFIGS__[config_name]
