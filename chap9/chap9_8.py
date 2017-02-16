#coding=utf-8
'''
Created on 2017��2��14��

@author: zhao
'''
import os
module_name=raw_input("enter module name")
print "attributes: ",dir(module_name)
with open(module_name):
    pwd=os.getcwdu()
    path_list=os.listdir(pwd)
    for i in path_list:
        print dir(i),i.__class__,i