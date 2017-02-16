#coding=utf-8
'''
Created on 2017��2��14��

@author: zhao
'''
init_dict={}
fobj=raw_input("enter file")
with open(fobj) as f:
    for i in f:
        config=i.split("=")
        init_dict[config[0]]=config[1].strip()
print init_dict