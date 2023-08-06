#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/10 3:29 PM
# @Author  : cw
import pytest


@pytest.mark.base
@pytest.mark.parametrize("name", ["小文base", "小曾base", "小s-base"])
def test_base(name):
    """我是test_base"""
    print(name)


@pytest.mark.all
@pytest.mark.parametrize("name", ["小文all", "小曾all", "小s-all"])
def test_all(name):
    """我是test_all"""
    print(name)


@pytest.mark.base
@pytest.mark.all
@pytest.mark.parametrize("name", ["小文all-base", "小曾all-base", "小s_all-base"])
def test_all_base(name):
    """我是test_all_base"""
    print("我是test_all_base")
    assert 1 == 1


@pytest.mark.base
@pytest.mark.initial
def test_skip():
    """我是test_skip"""
    print(342424242424)
    assert 2 == 2


@pytest.mark.cleanup
@pytest.mark.parametrize("project", ['project'])
@pytest.mark.parametrize("product", ['product'])
def test_cleanup(project, product):
    """清理vdc/vpc"""
    print(project, '88888888888888888')
    action = "DeletePrivateNetwork"
    method = "GET"
    param = {
        "PrivateId": 'pri_id'
    }
    assert 1 == 2
