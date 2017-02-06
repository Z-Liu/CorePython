#coding=utf-8
'''
Created on 2016��11��20��

@author: zhao
'''
input_string = raw_input('enter your string')
for x in zip(input_string, reversed(input_string)):
    print x