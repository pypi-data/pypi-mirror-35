#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `oceandb_driver_interface` package."""

from pytest import mark, raises
from oceandb_driver_interface.utils import parse_config


def test_oceandb_expects_plugin():
    from oceandb_driver_interface.plugin import AbstractPlugin
    with raises(TypeError):
        AbstractPlugin()


def test_oceandb_expcects_subclassed_plugin():
    from oceandb_driver_interface.plugin import AbstractPlugin

    class NonSubclassPlugin():
        pass

    plugin = NonSubclassPlugin()
    with raises(TypeError):
        AbstractPlugin(plugin)

def test_parse_config():
    config = parse_config('./tests/oceandb.ini')
    assert config['module'] == 'bigchaindb'
    assert config['db.hostname'] == 'localhost'