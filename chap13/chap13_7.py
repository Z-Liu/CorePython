#coding=utf-8
'''
Created on 2017��3��8��

@author: zhao
'''
from time import ctime
class Date(object):
    def __init__(self,dateTime=ctime()):
        self.dateTime=dateTime