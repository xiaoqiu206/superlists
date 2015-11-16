# coding=utf-8
'''
Created on 2015年11月16日

@author: xiaoq
'''
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
