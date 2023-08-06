#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oceandb_driver_interface.oceandb import OceanDb

mongo = OceanDb('./tests/oceandb.ini').plugin()


def test_plugin_type_is_mongodb():
    assert mongo.type == 'MongoDB'


def test_plugin_write_and_read():
    did = 'did:ocn-asset:0x123456789abcdefghi#path1'
    mongo.write({"value": "test"}, did)
    assert mongo.read(did)['_id'] == did
    assert mongo.read(did)['value'] == 'test'
    mongo.delete(did)


def test_update():
    mongo.write({"value": "test"}, 1)
    assert mongo.read(1)['value'] == 'test'
    mongo.update({"value": "testUpdated"}, 1)
    assert mongo.read(1)['value'] == 'testUpdated'
    mongo.delete(1)


def test_plugin_list():
    mongo.write({"value": "test1"}, 1)
    mongo.write({"value": "test2"}, 2)
    mongo.write({"value": "test3"}, 3)
    assert mongo.list().count() == 3
    assert mongo.list()[0]['value'] == 'test1'
    mongo.delete(1)
    mongo.delete(2)
    mongo.delete(3)

def test_plugin_query():
    mongo.write({'example': 'mongo'}, 1)
    assert mongo.query({'example': 'mongo'})[0]['example'] == "mongo"
    mongo.delete(1)
