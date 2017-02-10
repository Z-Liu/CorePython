#coding=utf-8
'''
Created on 2017年2月9日

@author: zhao
'''
def fibonacci(n):
    a=1
    b=1
    if n in [1,2]:
        return 1
    while n>2:
        b,a=a+b,b
        n-=1
    return b

print fibonacci(6)
print fibonacci(8)