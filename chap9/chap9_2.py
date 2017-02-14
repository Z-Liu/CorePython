#coding=utf-8
'''
Created on 2017��2��13��

@author: zhao
'''
def read_file(N,F):
    with open(F) as f:
        for i in range(N):
            print f.readline(),

print read_file(10, "chap9_2")