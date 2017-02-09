#coding=utf-8
'''
Created on 2017��2��8��

@author: zhao
'''
three_value = raw_input("enter from, to, increment")
three_value = three_value.split(",")
f = int(three_value[0])
t = int(three_value[1])
i = int(three_value[2])
for j in range(f,t+1,i):
    print j