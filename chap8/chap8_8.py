#coding=utf-8
'''
Created on 2017��2��9��

@author: zhao
'''
def factorial(number):
    res=1
    for i in range(2,number+1):
        res*=i
    return res

if __name__ == '__main__':
    number=int(raw_input("enter number"))
    print factorial(number)