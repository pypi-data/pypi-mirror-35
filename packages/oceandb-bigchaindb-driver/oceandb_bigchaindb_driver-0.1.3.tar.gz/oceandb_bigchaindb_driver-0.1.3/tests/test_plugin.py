#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oceandb_driver_interface.oceandb import OceanDb

bdb = OceanDb('./tests/oceandb.ini').plugin()


def test_plugin_type_is_bdb():
    assert bdb.type == 'BigchainDB'


def test_plugin_write_and_read():
    bdb.write({"value": "plugin"}, 1)
    assert bdb.read(1)['value'] == 'plugin'
    bdb.delete(1)


def test_update():
    bdb.write({"value": "test"}, 2)
    assert bdb.read(2)['value'] == 'test'
    bdb.update({"value": "testUpdated"}, 2)
    bdb.update({"value": "testUpdated2"}, 2)
    assert bdb.read(2)['value'] == 'testUpdated2'
    bdb.delete(2)


def test_plugin_list():
    bdb.write({"value": "test1"}, 3)
    bdb.update({"value": "testUpdated"}, 3)
    bdb.write({"value": "test2"}, 4)
    bdb.write({"value": "test3"}, 5)
    assert len(bdb.list()) == 3
    assert bdb.list()[0]['value'] == 'testUpdated'
    bdb.delete(3)
    bdb.delete(4)
    bdb.delete(5)
    assert len(bdb.list()) == 0


def test_plugin_query():
    bdb.write({'example': 'BDB'}, 6)
    assert bdb.query('BDB')[0]['data']['example'] == "BDB"
    bdb.delete(6)
