#coding=utf-8
'''
Created on 2017��2��7��

@author: zhao
'''
dict_a={
    "a":1,
    "b":2,
    "c":3
    }
dict_b={}
for i in dict_a:
    dict_b[dict_a[i]] = i
print dict_b