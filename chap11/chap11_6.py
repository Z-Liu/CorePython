#coding=utf-8
'''
Created on 2017��2��21��

@author: zhao
'''
def printf(string,*rest):
    return string%rest
print printf("this %s %d test %s","is",1,"string")