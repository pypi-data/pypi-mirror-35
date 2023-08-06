# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 下午3:10
# @Author  : Shark
# @File    : RefreshEnt.py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from selenium import webdriver
import json
import time
from urllib import quote
import argparse
from urllib import unquote

class RefreshEnt(object):

    keys = ['sb', 'c_user', 'xs', 'fr', 'pl', 'spin','presence','datr','dpr']

    retry = 3

    def __init__(self,url,cookies):
        self.url = url
        temporary = eval(cookies)
        self.cookies = []
        for name in temporary.keys():
            self.cookies.append({'name':name,'value':temporary[name]['value'],'expiry':temporary[name]['expiry'],'domain':temporary[name]['domain'],'path':temporary[name]['path']})

    def refresh(self):
        dict = {}
        for i in range(3):
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            browser = webdriver.Chrome(chrome_options=options)
            browser.get(self.url)
            for cookie in self.cookies:
                browser.add_cookie(cookie)
            browser.get(self.url)
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
                        tuples.append((name, value, expiry, path, domain))
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
    ##temporary = eval(cookies)
    ##for key in temporary.keys():
    ##    pass
    '''
    timestamp = int(time.time())
    print str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)))
    timestamp = str(timestamp)
    url = 'https://www.facebook.com/king.rawle/friends?lst=' + quote('100011477435504:100001550031652:%(t)s' % {
        't': timestamp
    }) + '&source_ref=pb_friends_tl'
    cookies = '{"c_user": {"path": "/", "domain": ".facebook.com", "value": "100011477435504", "expiry": "1542771854.14"}, "fr": {"path": "/", "domain": ".facebook.com", "value": "0VqyjlWoOjlpgcYEb.AWVIAOF4UICWtleU7ijZ8T22RJc.Bbfi2K.Vl.AAA.0.0.Bbfi2O.AWXpq4SW", "expiry": "1542771854.14"}, "dpr": {"path": "/", "domain": ".facebook.com", "value": "2", "expiry": "1535600654"}, "presence": {"path": "/", "domain": ".facebook.com", "value": "EDvF3EtimeF1534995860EuserFA21B11477435504A2EstateFDutF1534995859975CEchFDp_5f1B11477435504F0CC", "expiry": ""}, "datr": {"path": "/", "domain": ".facebook.com", "value": "ii1-W5QNd72cwiCMAeXZL7ec", "expiry": "1598067854.14"}, "sb": {"path": "/", "domain": ".facebook.com", "value": "ii1-W7DLYtyCK6Gs7gdoBVzx", "expiry": "1598067854.14"}, "xs": {"path": "/", "domain": ".facebook.com", "value": "46%3A6x7O7UTIiD74qA%3A2%3A1534995854%3A-1%3A-1", "expiry": "1542771854.14"}, "spin": {"path": "/", "domain": ".facebook.com", "value": "r.4239339_b.trunk_t.1534995855_s.1_v.2_", "expiry": "1535085855.39"}, "pl": {"path": "/", "domain": ".facebook.com", "value": "n", "expiry": "1542771854.14"}}'
    refresh = RefreshEnt(url,cookies)
    str = refresh.refresh()
    print(str)
    '''
    parser = argparse.ArgumentParser(description='facebook用户登录')
    parser.add_argument('--url', type=str, default=None)
    parser.add_argument('--cookies', type=str, default=None)
    args = parser.parse_args()
    url = args.url
    cookies = args.cookies
    cookies = unquote(cookies)
    refresh = RefreshEnt(url, cookies)
    str = refresh.refresh()
    print(str)




