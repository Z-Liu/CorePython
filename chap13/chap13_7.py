#coding=utf-8
'''
Created on 2017Äê3ÔÂ8ÈÕ

@author: zhao
'''
from time import ctime
class Date(object):
    def __init__(self,dateTime=ctime()):
        self.dateTime=dateTime