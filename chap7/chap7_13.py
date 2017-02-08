#coding=utf-8
'''
Created on 2017��2��8��

@author: zhao
'''
from random import randrange, randint

a = {randint(1,10) for i in range(randrange(9))}
b = {randint(1,10) for i in range(randrange(9))}
print a
print b
print a|b
print a&b