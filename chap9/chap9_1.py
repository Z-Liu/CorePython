#coding=utf-8
'''
Created on 2017年2月13日

@author: zhao
'''
with open("chap9_1") as f:
    for x in f:
        if x[0]!="#":
            e=x.find("#")
            print x[0:e]
            
