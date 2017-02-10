#coding=utf-8
'''
Created on 2017��2��9��

@author: zhao
'''
def count(string):
    return sum(1 for i in string if i==" " or i==".")
print count("what a good day.")
        