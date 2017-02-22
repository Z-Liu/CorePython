#coding=utf-8
'''
Created on 2017��2��21��

@author: zhao
'''
def average(numbers):
    return reduce((lambda x,y:x+y),numbers)/float(len(numbers))
print average([2,3,4,5])