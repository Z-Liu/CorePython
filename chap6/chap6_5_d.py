#coding=utf-8
'''
Created on 2016��11��22��

@author: zhao
'''
def func(a_string):
    return a_string + a_string[::-1]

if __name__ == '__main__':
    a = raw_input('prompt')
    print func(a)