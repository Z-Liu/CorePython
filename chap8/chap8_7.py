#coding=utf-8
'''
Created on 2017��2��9��

@author: zhao
'''
from chap8.chap8_5 import getfactors
def isperfect(number):
    return int(number==sum(getfactors(number)[:-1]))

if __name__ == '__main__':
    number=int(raw_input("enter number"))
    print isperfect(number)