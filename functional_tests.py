# coding=utf-8
'''
Created on 2015年11月16日

@author: xiaoq
'''
from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()