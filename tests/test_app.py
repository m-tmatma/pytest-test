#!/usr/bin/python
# -*- coding: utf-8 -*-

def test_1():
    a = 1
    b = 2
    assert a != b

def test_target(target):
    print(target)
    #assert target == 'hogehoge'

# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print(tmpdir)
    #assert 0
