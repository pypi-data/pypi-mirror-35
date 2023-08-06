# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午7:32
# @Author  : Shark
# @File    : __init__.py.py
from Filter import Filter

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class FilterClient(object):

    def __init__(self,host,port):
        transport1 = TSocket.TSocket(host, port)
        transport2 = TTransport.TBufferedTransport(transport1)
        protocol = TBinaryProtocol.TBinaryProtocol(transport2)
        self.client = Filter.Client(protocol)
        transport2.open()
        self.transport = transport2

    def has(self,val):
        return self.client.has(val)

    def contain(self,val):
        return self.client.contain(val)

    def add(self,val):
        return self.client.add(val)

    def close(self):
        self.transport.close()



if __name__ == '__main__':

    host = 'localhost'
    port = 9099
    filter = FilterClient(host,port)
    print str(filter.has('test'))
    filter.add('test')
    filter.close()
