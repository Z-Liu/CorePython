#coding=utf-8
'''
Created on 2017��3��1��

@author: zhao
'''
def importAs(aModule):
   return __import__(aModule) a=importAs('operator')
print a.add(3,2)