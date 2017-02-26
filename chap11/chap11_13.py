#coding=utf-8
'''
Created on 2017��2��23��

@author: zhao
'''
import time
def timeit(func,*args,**kwargs):
    begin_time=time.clock()
    res=func(*args,**kwargs)
    end_time=time.clock()
    return end_time-begin_time
def mult(x,y):
    return x*y
def factorial(n):
    factorialList=[i+1 for i in range(n)]
    return reduce(mult,factorialList)
def factorial1(n):
    factorialList=[i+1 for i in range(n)]
    return reduce(lambda x,y:x*y,factorialList)
def factorial2(n):
    if n>1:
        return n*factorial2(n-1)
    else:
        return 1
print timeit(factorial,500)
print timeit(factorial1,500)
print timeit(factorial2,500)