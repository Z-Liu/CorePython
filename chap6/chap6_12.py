#coding=utf-8
'''
Created on 2016��11��27��

@author: zhao
'''
import unittest
def findchr(string, char):
    i=-1
    for j in string:
        i+=1
        if j==char:
            return i
    return -1
def rfindchr(string, char):
    i=len(string)
    for j in string[::-1]:
        i-=1
        if j==char:
            return i
    return -1
def subchr(string, origchar, newchar):
    new_string=""
    for j in string:
        if j!=origchar:
            new_string+=j
        else:
            new_string+=newchar
    return new_string

if __name__ == '__main__':
    string=raw_input("enter")
    print findchr(string, "s"), rfindchr(string, "s"), subchr(string, "s", "e")