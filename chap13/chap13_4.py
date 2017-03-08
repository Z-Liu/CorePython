#coding=utf-8
'''
Created on 2017��3��6��

@author: zhao
'''
class Database(object):
    def __init__(self,data="data.txt"):
        self.data=data
        self.buffer=[]
    def add(self,user):
        if user in open(self.data).readlines() or user in self.buffer:
            print "already exsits"
        else:
            self.buffer.append(user)
            print "succeed"
    def __del__(self):
        with open(self.data,"a") as f:
            f.writelines(self.buffer)