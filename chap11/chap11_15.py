#coding=utf-8
'''
Created on 2017��2��26��

@author: zhao
'''
def printStringForwardAndBackward(string):
    if len(string)==1:
        return string+string
    else:
        return string[0]+printStringForwardAndBackward(string[1:])+\
        string[0]
print printStringForwardAndBackward("string")