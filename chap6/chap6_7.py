#coding=utf-8
'''
Created on 2016年11月23日

@author: zhao
'''
#buggy.py
num_str = raw_input("enter a number:")
num_num = int(num_str)
non_fac_list = range(1, num_num+1)
print "BEFORE:", repr(non_fac_list)
i = 0
while i < len(non_fac_list):
    if num_num%non_fac_list[i]==0:
        del non_fac_list[i]
    else:
        i = i+1
print "AFTER:", repr(non_fac_list)