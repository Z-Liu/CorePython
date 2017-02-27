#coding=utf-8
'''
Created on 2017��2��26��

@author: zhao
'''
def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print fibonacci(6)
print fibonacci(8)