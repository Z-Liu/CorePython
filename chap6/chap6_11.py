#coding=utf-8
'''
Created on 2016��11��26��

@author: zhao
'''
def func(a_integer):
    long_integer = "%012d"%(a_integer)
    internet_protocol = ".".join((long_integer[0:3],long_integer[3:6],long_integer[6:9],long_integer[9:12]))
    return internet_protocol
    
def func1(a_str):
    return int(a_str.replace(".",""))
    
if __name__ == '__main__':
#     a_integer = int(raw_input("prompt"))
#     print func(a_integer)    
    a_str = raw_input("prompt")
    print func1(a_str)
    