# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/27 下午4:25
# @Author  : Mori
# @Email   : moridisa@moridisa.cn
# @File    : data_operator.py
# @Software: PyCharm
# @Desc    : data operator

import odps
import redis
import pymysql
import pymongo
from redis import Redis as RedisClient
from odps import ODPS as ODPSClient
from pymysql.connections import Cursor as MysqlCursor
from pymongo.collection import Collection as MongoCollection
from typing import List
from .utils import read_config, arg_check

__all__ = [
    'MysqlCursor',
    'MongoCollection',
    'RedisClient',
    'execute_mysql',
    'query_mysql',
    'query_mongo',
    'query_odps',
    'get_mysql_db_name',
    'get_zookeeper_host',
    'conn_mysql',
    'conn_mongo',
    'conn_redis',
    'conn_odps'
]


def __get_odps_connection(config_name: str) -> ODPSClient:
    """
    make odps connection instance

    :param config_name: config name
    :return: odps connection_instance
    """
    config = read_config(config_name)
    arg_check(config_name, ['access_key_id', 'access_key_secret', 'project_name', 'end_point'])

    return odps.ODPS(config['access_key_id'], config['access_key_secret'], config['project_name'], config['end_point'])


def __get_mysql_connection(config_name: str) -> pymysql.Connection:
    """
    load mysql config & make a mysql connection

    :param config_name: config name in yaml
    """
    config = read_config(config_name)
    arg_check(config_name, ['db', 'host', 'port', 'user', 'passwd'])

    return pymysql.connect(**config)


def __get_mongo_connection(config_name: str) -> pymongo.MongoClient:
    """
    connection to mongo

    :param config_name: config name in yaml
    :return: mongo client
    """
    config = read_config(config_name)
    arg_check(config_name, ['host', 'username', 'password', 'auth'])

    client = pymongo.MongoClient('mongodb://' + config['host'])
    client[config['auth']].authenticate(config['username'], config['password'])

    return client


def __get_redis_connection(config_name: str, db: int = None) -> RedisClient:
    """
    connection to redis

    :param config_name: config name in yaml
    :param db: db
    :return: redis client
    """
    config = read_config(config_name)
    check_args = ['host', 'port', 'auth']
    if db is None: check_args.append('db')
    arg_check(config_name, check_args)
    t_db = config['db'] if db is None else db

    return redis.Redis(host=config['host'], port=config['port'], db=t_db, password=config['auth'])


conn_odps = __get_odps_connection
conn_mysql = __get_mysql_connection
conn_mongo = __get_mongo_connection
conn_redis = __get_redis_connection


def get_zookeeper_host(config_name: str) -> str:
    """
    get zookeeper host

    :param config_name: config name in yaml
    :return: zookeeper host
    """
    arg_check(config_name, ['keeper_list'])
    return read_config(config_name)['keeper_list'].split(',')[0]


def get_mysql_db_name(config_name: str) -> str:
    """
    get mysql db name in config

    :param config_name: config name in yaml
    :return: 'db' in yaml
    """
    arg_check(config_name, ['db'])
    return read_config(config_name)['db']


def query_mysql(config_name: str, sql: str, use_dict: bool = False) -> List:
    """
    query on mysql

    :param config_name: config name in yaml
    :param sql: sql
    :param use_dict: use dict data
    :return: query result
    """
    conn = conn_mysql(config_name)
    with conn:
        if use_dict:
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            cursor = conn.cursor()
        with cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    return result


def query_odps(config_name: str, sql: str, use_dict: bool = False) -> List:
    """
    query on odps

    :param config_name: config name in yaml
    :param sql: sql
    :param use_dict: use dict data
    :return: query result
    """
    instance = conn_odps(config_name)
    result = []
    with instance.execute_sql(sql).open_reader(use_tunnel=True, limit_enabled=False) as reader:
        if use_dict:
            for record in reader:
                result.append(dict(record))
        else:
            for record in reader:
                result.append(record.values)
    return result


def query_mongo(config_name: str, condition: dict, collection_name: str = None) -> List:
    """
    query on mongo

    :param config_name: config name in yaml
    :param condition: query condition
    :param collection_name: collection name in mongo
    :return: query result
    """
    config = read_config(config_name)
    result = []

    check_args = ['db']
    if collection_name is not None: check_args.append('collection')
    arg_check(config_name, check_args)

    with conn_mongo(config_name) as mongo_client:
        db = mongo_client.get_database(config['db'])
        collection = db.get_collection(
            collection_name if collection_name is not None else config['collection'])
        cursor = collection.find(condition)
        for record in cursor:
            result.append(record)
        cursor.close()
    return result


def execute_mysql(config_name: str, sql: str) -> int:
    """
    :param config_name: config name in yaml
    :param sql: sql
    :return: return last id if sql.startwith('insert') else effect_row
    """
    conn = conn_mysql(config_name)
    with conn:
        cursor = conn.cursor()
        with cursor:
            effect_row = cursor.execute(sql)
            if sql.lower().startswith('insert'):
                effect_row = cursor.lastrowid
        conn.commit()
    return effect_row
