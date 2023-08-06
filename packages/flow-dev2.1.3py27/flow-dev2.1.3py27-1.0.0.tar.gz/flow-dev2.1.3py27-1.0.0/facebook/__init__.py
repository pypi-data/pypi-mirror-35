# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 下午2:53
# @Author  : Shark
# @File    : __init__.py.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import argparse

from facebook.Login import Login
from facebook.RefreshEnt import RefreshEnt

from urllib import unquote

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=str, default=None)
    parser.add_argument('--user', type=str, default=None)
    parser.add_argument('--passwd', type=str, default=None)
    parser.add_argument('--url', type=str, default=None)
    parser.add_argument('--cookies', type=str, default=None)
    args = parser.parse_args()
    m = args.m
    if m == 'login':
        user = args.user
        passwd = args.passwd
        login = Login(user, passwd)
        str = login.login()
        print(str)
    elif m == 'refresh':
        url = args.url
        cookies = args.cookies
        cookies = unquote(cookies)
        refresh = RefreshEnt(url,cookies)
        str = refresh.refresh()
        print(str)
    else:
        print('-1')



