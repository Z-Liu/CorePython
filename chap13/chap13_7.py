#coding=utf-8
'''
Created on 2017��3��8��

@author: zhao
'''
from datetime import datetime
class Date(object):
    def __init__(self,*dateTime):
        self.dateTime=datetime(dateTime)
    def update(self,*dateTime):
        self.dateTime=datetime(dateTime)
    def display(self,theFormat="default"):
        formatMap={"MDY":,
                   "MDYY":,
                   "DMY":,
                   "DMYY":,
                   "MODYY":,
                   "default":
                        }
        dateStr=str((self.dateTime).date())