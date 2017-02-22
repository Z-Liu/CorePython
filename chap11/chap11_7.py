#coding=utf-8
'''
Created on 2017��2��21��

@author: zhao
'''
def a_map(list_a,list_b):
    return map(None, list_a, list_b)
def a_zip(list_a,list_b):
    return zip(list_a,list_b)
list_a=[1,2,3]
list_b=['abc','def','ghi']
print a_map(list_a,list_b)
print a_zip(list_a,list_b)