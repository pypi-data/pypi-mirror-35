#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      mongo_client.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 4, 2018
    @desc:      Mongodb storage access class
"""

import logging
import motor.motor_asyncio as motor

from tomato.utils import singleton


@singleton
class MongoClient(object):
    """
    Use examples

    mongodb = MongoClient(address='10.0.0.1:27017,10.0.0.2:27017,10.0.0.3:27017')
    mongodb.insert(item) // insert item
    """

    def __init__(self, address,
                 user=None,
                 passwd=None,
                 replicat_set=None,
                 min_pool_size=1,
                 max_pool_size=1,
                 auth_source=None,
                 auth_mechanism='SCRAM-SHA-1'):

        if not isinstance(address, str) or len(address) == 0:
            logging.error('address field is invalid[%s]', address)
            return

        address = address.split(',')
        self.client = motor.AsyncIOMotorClient(address, authSource=auth_source,
                                               username=user,
                                               password=passwd,
                                               replicaSet=replicat_set,
                                               minPoolSize=min_pool_size,
                                               maxPoolSize=max_pool_size,
                                               authMechanism=auth_mechanism)
        logging.info('Mongo Client init info[%s]', address)

    async def find_one(self, database=None,
                       collection=None,
                       key=None,
                       fields=None,
                       network_timeout=5):
        collection = self.client[database][collection]
        if fields is None:
            future = collection.find_one(key, max_time_ms=network_timeout)
        else:
            future = collection.find_one(key, fields, max_time_ms=network_timeout)
        try:
            doc = await future
        except Exception as e:
            logging.error('[%s]', str(e))
            raise
        else:
            return doc

    async def find(self, database=None,
                   collection=None,
                   key=None,
                   fields=None,
                   start=0,
                   count=0,
                   sort_item=None,
                   total=0,
                   network_timeout=5,
                   batch_size=10):
        docs = []
        collection = self.client[database][collection]
        if fields is None:
            if sort_item is not None:
                cursor = collection.find(key, max_time_ms=network_timeout, skip=start, limit=count).sort(sort_item)
            else:
                cursor = collection.find(key, max_time_ms=network_timeout, skip=start, limit=count)
        else:
            if sort_item is not None:
                cursor = collection.find(key, fields, max_time_ms=network_timeout, skip=start, limit=count).sort(sort_item)
            else:
                cursor = collection.find(key, fields, max_time_ms=network_timeout, skip=start, limit=count)
        try:
            cursor.batch_size(batch_size)
            while (await cursor.fetch_next):
                docs.append(cursor.next_object())
        except Exception as e:
            logging.error('[%s]', str(e))
            raise

        total_count = None
        if total == 1:
            cursor = collection.find(key, max_time_ms=network_timeout).count()
            try:
                total_count = await cursor
            except Exception as e:
                logging.error('[%s]', str(e))
                raise
            return (total_count, docs)
        return docs

    async def insert(self, database=None,
                     collection=None,
                     ins_item=None,
                     network_timeout=5):
        try:
            collection = self.client[database][collection]
            result = await collection.insert_one(ins_item)
        except Exception as e:
            logging.error('[%s]', str(e))
            raise
        else:
            return result

    def _data_format(self, item, result, root_prefix='', path=''):
        for key in item:
            if '$' in root_prefix or key[0] == '$':
                root_prefix = '$'
            if isinstance(item[key], dict):
                if key[0] != '$' and path != '':
                    self._data_format(item[key], result, root_prefix=root_prefix, path='{}.{}'.format(path, key))
                elif key[0] == '$' and path != '':
                    if path in result:
                        result[path][key] = {}
                    else:
                        result[path] = {key: {}}
                    self._data_format(item[key], result[path][key], root_prefix=root_prefix, path='')
                elif key[0] == '$' and path == '':
                    result[key] = {}
                    self._data_format(item[key], result[key], root_prefix=root_prefix, path='')
                else:
                    self._data_format(item[key], result, root_prefix=root_prefix, path=key)
            elif key[0] == '$' and path != '':
                result[path] = {key: item[key]}
            elif key[0] != '$' and path != '':
                if root_prefix == '$':
                    result['{}.{}'.format(path, key)] = item[key]
                else:
                    if '$set' not in result:
                        result['$set'] = {}
                    result['$set']['{}.{}'.format(path, key)] = item[key]
            else:
                if key[0] != '$' and root_prefix != '$':
                    if '$set' not in result:
                        result['$set'] = {}
                    result['$set'][key] = item[key]
                else:
                    result[key] = item[key]

    async def update(self, database=None,
                     collection=None,
                     key=None,
                     up_item=None,
                     ins_item=None,
                     upsert=False,
                     multi=False,
                     network_timeout=5):
        collection = self.client[database][collection]
        data = {}
        if up_item:
            self._data_format(up_item, data)
        if ins_item:
            data['$setOnInsert'] = ins_item
        if multi == False:
            future = collection.update_one(key, data,
                                           upsert=upsert)  # wtimeout, w
        else:
            future = collection.update_many(key, data,
                                            upsert=upsert)  # wtimeout, w
        try:
            result = await future
        except Exception as e:
            logging.error('[%s]', str(e))
            raise
        else:
            return result

    async def remove(self, database=None,
                collection=None,
                key=None,
                network_timeout=5):
        collection = self.client[database][collection]
        future = collection.remove(key) # wtimeout, w
        try:
            result = await future
        except Exception as e:
            logging.error('[%s]', str(e))
            raise
        else:
            return result
