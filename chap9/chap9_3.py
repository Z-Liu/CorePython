#coding=utf-8
'''
Created on 2017��2��14��

@author: zhao
'''
fobj=raw_input("file name?")
with open(fobj) as f:
    print len(f.readlines())