#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

def test_github():
	r = requests.get('https://api.github.com/')
	
	print('https://api.github.com/')
	print(r.status_code)
	assert r.status_code == 200
	
	print(r.headers['content-type'])
	assert 'application/json' in r.headers['content-type']
	
	print(r.encoding)
	assert 'utf-8' in r.encoding

	print(r.json())
