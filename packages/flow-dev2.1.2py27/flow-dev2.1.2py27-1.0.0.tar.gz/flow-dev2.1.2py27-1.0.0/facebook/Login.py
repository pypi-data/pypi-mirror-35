# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 下午3:00
# @Author  : Shark
# @File    : Login.py
from selenium import webdriver
import json
import argparse

class Login(object):

    retry = 3

    keys = ['sb', 'c_user', 'xs', 'fr', 'pl', 'spin','presence','datr','dpr']

    def __init__(self,user,passwd):
        self.user = user
        self.passwd = passwd

    def login(self):
        dict = {}
        for i in range(3):
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            browser = webdriver.Chrome(chrome_options=options)
            browser.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
            element = browser.find_element_by_id('email')
            element.send_keys(self.user)
            element1 = browser.find_element_by_id('pass')
            element1.send_keys(self.passwd)
            element2 = browser.find_element_by_id('loginbutton')
            element2.send_keys('loginbutton')
            element2.click()
            cookies = browser.get_cookies()
            tuples = []
            for cookie in cookies:
                if u'expiry' not in cookie.keys():
                    cookie[u'expiry'] = ''
                if u'domain' not in cookie.keys():
                    cookie[u'domian'] = ''
                if u'path' not in cookie.keys():
                    cookie[u'path'] = ''

                value = cookie[u'value'].encode('UTF-8')
                expiry = str(cookie[u'expiry'])
                name = cookie[u'name'].encode('UTF-8')
                domain = cookie[u'domain'].encode('UTF-8')
                path = cookie[u'path'].encode('UTF-8')
                for name1 in self.keys:
                    if name == name1:
                        tuples.append((name, value, expiry,path,domain))
            browser.close()
            for tuple in tuples:
                name = tuple[0]
                value = tuple[1]
                expiry = tuple[2]
                path = tuple[3]
                domain = tuple[4]
                for key in self.keys:
                    if name == key:
                        dict1 = {}
                        dict1['value'] = value
                        dict1['expiry'] = expiry
                        dict1['path'] = path
                        dict1['domain'] = domain
                        dict[name] = dict1
            break
        return json.dumps(dict)


if __name__ == '__main__':
    '''
    user = '13240164061'
    passwd = 'heng0516..'
    login = Login(user,passwd)
    str = login.login()
    print(str)
    
    parser = argparse.ArgumentParser(description='facebook用户登录')
    parser.add_argument('--user', type=str, default=None)
    parser.add_argument('--passwd', type=str, default=None)
    args = parser.parse_args()
    user = args.user
    passwd = args.passwd
    login = Login(user, passwd)
    str = login.login()
    print(str)
    '''
    dict = {}
    keys = ['sb', 'c_user', 'xs', 'fr', 'pl', 'spin', 'presence', 'datr', 'dpr']
    user = '13240164061'
    passwd = 'heng0516..'
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=options)
    browser.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
    element = browser.find_element_by_id('email')
    element.send_keys(user)
    element1 = browser.find_element_by_id('pass')
    element1.send_keys(passwd)
    element2 = browser.find_element_by_id('loginbutton')
    element2.send_keys('loginbutton')
    element2.click()
    cookies = browser.get_cookies()
    tuples = []
    for cookie in cookies:
        if u'expiry' not in cookie.keys():
            cookie[u'expiry'] = ''
        if u'domain' not in cookie.keys():
            cookie[u'domian'] = ''
        if u'path' not in cookie.keys():
            cookie[u'path'] = ''

        value = cookie[u'value']
        expiry = cookie[u'expiry']
        name = cookie[u'name']
        domain = cookie[u'domain']
        path = cookie[u'path']
        for name1 in keys:
            if name == name1:
                tuples.append((name, value, expiry, path, domain))
    browser.close()
    for tuple in tuples:
        print(tuple)
    for tuple in tuples:
        name = tuple[0]
        value = tuple[1]
        expiry = tuple[2]
        path = tuple[3]
        domain = tuple[4]
        for key in keys:
            if name == key:
                dict1 = {}
                dict1['value'] = value
                dict1['expiry'] = expiry
                dict1['path'] = path
                dict1['domain'] = domain
                dict[name] = dict1
    print(json.dumps(dict))
