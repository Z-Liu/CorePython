#coding=utf-8
'''
Created on 2017��2��15��

@author: zhao
'''
def max2(a,b):
    if a>b:
        return a
    else:
        return b
def min2(a,b):
    if a>b:
        return b
    else:
        return a
def my_max(*args):
    res=args[0]
    for i in args:
        res=max(i,res)
    return res
def my_min(*args):
    res=args[0]
    for i in args:
        res=min(i,res)
    return res

print max(1,2)
print max("a","b")
print min(1,2)
print min("a","b")
print my_max(1,2,3)
print my_max("a","b","c")
print my_min(1,2,3)
print my_min("a","b","c")