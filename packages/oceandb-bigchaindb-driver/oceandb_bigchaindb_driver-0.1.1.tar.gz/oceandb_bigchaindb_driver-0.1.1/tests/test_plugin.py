#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oceandb_driver_interface.oceandb import OceanDb

bdb = OceanDb('./tests/oceandb.ini').plugin


def test_plugin_type_is_bdb():
    assert bdb.type == 'BigchainDB'


def test_plugin_write_and_read():
    bdb.write({"value": "plugin"}, resource_id=1)
    assert bdb.read(resource_id=1)['data']['data']['value'] == 'plugin'
    bdb.delete(1)


def test_update():
    bdb.write({"value": "test"}, resource_id=2)
    assert bdb.read(resource_id=2)['data']['data']['value'] == 'test'
    bdb.update({"value": "testUpdated"}, 2)
    bdb.update({"value": "testUpdated2"}, 2)
    assert bdb.read(resource_id=2)['data']['data']['value'] == 'testUpdated2'
    bdb.delete(2)


def test_plugin_list():
    bdb.write({"value": "test1"},resource_id=3)
    bdb.update({"value": "testUpdated"}, 3)
    bdb.write({"value": "test2"}, resource_id=4)
    bdb.write({"value": "test3"}, resource_id=5)
    assert len(bdb.list()) == 3
    assert bdb.list()[0]['data']['data']['value'] == 'testUpdated'
    bdb.delete(3)
    bdb.delete(4)
    bdb.delete(5)
    assert len(bdb.list()) == 0


def test_plugin_query():
    bdb.write({'example': 'BDB'}, resource_id=6)
    assert bdb.query('BDB')[0]['data']['example'] == "BDB"
    bdb.delete(6)
