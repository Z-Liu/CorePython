#coding=utf-8
'''
Created on 2017��2��22��

@author: zhao
'''
import time
def timeit(func,*args,**kwargs):
    begin_time=time.clock()
    res=func(*args,**kwargs)
    end_time=time.clock()
    return res, end_time-begin_time

def f(a,b=2):
    return a**b

print timeit(f,2)
print timeit(f,2,10)