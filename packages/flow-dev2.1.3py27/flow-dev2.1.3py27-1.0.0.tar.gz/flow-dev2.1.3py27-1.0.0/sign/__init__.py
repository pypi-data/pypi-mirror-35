# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 下午5:31
# @Author  : Shark
# @File    : __init__.py.py
import re
from urllib import quote
import hashlib

def sign_xiaohongshu(form):
    dict = {}
    params = re.split('&',form)
    for _ in params:
        tuple = re.split('=',_)
        dict[tuple[0]] = tuple[1]
    keys = dict.keys()
    keys.sort()
    params1 = []
    for _ in keys:
        params1.append(_ + '=' + dict[_])
    form= ''.join(params1)
    device_id = dict['deviceId']
    form = quote(form)
    bytes = []
    for _ in form:
        bytes.append(ord(_))
    bytes1 = []
    for _ in device_id:
        bytes1.append(ord(_))
    temporary = ''
    for i in range(0, len(bytes)):
        temporary = temporary + str(bytes[i] ^ bytes1[i % len(bytes1)])
    hl = hashlib.md5()
    hl.update(temporary.encode(encoding='utf-8'))
    first = hl.hexdigest()
    temporary = first + device_id
    hl = hashlib.md5()
    hl.update(temporary.encode(encoding='utf-8'))
    return hl.hexdigest()


if __name__ == '__main__':
    '''
    from urllib import quote
    import hashlib
    form = 'deviceId=A5E84D5C-FCE3-4C27-A6C4-699AF3816AE3device_fingerprint=20180720152741833d301f7cfc0a1ba1893d811f505ea801f94af1b6f08c44device_fingerprint1=20180720152741833d301f7cfc0a1ba1893d811f505ea801f94af1b6f08c44keyword=皇冠假日keyword_type=normallang=zhpage=1page_size=20platform=iOSsearch_id=594CF03B78F01CFAC4049B9869FBD8A2sid=session.1216567949652537531sort=time_descendingsource=explore_feedt=1532140494'
    device_id = 'A5E84D5C-FCE3-4C27-A6C4-699AF3816AE3'
    form = quote(form)
    bytes = []
    for _ in form:
        bytes.append(ord(_))
    bytes1 = []
    for _ in device_id:
        bytes1.append(ord(_))
    temporary = ''
    for i in range(0, len(bytes)):
        temporary = temporary + str(bytes[i] ^ bytes1[i % len(bytes1)])
    hl = hashlib.md5()
    hl.update(temporary.encode(encoding='utf-8'))
    first = hl.hexdigest()
    temporary = first + device_id
    hl = hashlib.md5()
    hl.update(temporary.encode(encoding='utf-8'))
    print('MD5加密后为 ：' + hl.hexdigest())
    '''
    form = 'deviceId=A5E84D5C-FCE3-4C27-A6C4-699AF3816AE3&device_fingerprint=20180720152741833d301f7cfc0a1ba1893d811f505ea801f94af1b6f08c44&device_fingerprint1=20180720152741833d301f7cfc0a1ba1893d811f505ea801f94af1b6f08c44&lang=zh&platform=iOS&sid=session.1216567949652537531&size=l&t=1532140602'
    print(sign_xiaohongshu(form))








