#coding=utf-8
'''
Created on 2017��2��9��

@author: zhao
'''
from chap8.chap8_4 import isprime
from chap8.chap8_5 import getfactors
def primeAnaly(number):
    factors=getfactors(number)
    primeFactors=[]
    for i in factors:
        if isprime(i):
            primeFactors.append(i)
    res=[]
    while number!=1:
        for i in primeFactors:
            if number%i==0: 
                number/=i
                res.append(i)
    return res

if __name__ == '__main__':
    number=int(raw_input("enter number"))
    print primeAnaly(number)