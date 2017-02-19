#coding=utf-8
'''
Created on 2017��2��15��

@author: zhao
'''
def transform(minutes):
    hour,minute=divmod(minutes,60)
    return hour,minute
print transform(720)
print transform(1403)