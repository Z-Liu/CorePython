#coding=utf-8
'''
Created on 2017��2��7��

@author: zhao
'''
staff = {"a":1,
         "d":4,
         "c":5,
         "b":3,
         "e":7
    }
sorted_staff = sorted(staff.keys())
for i in sorted_staff:
    print "%s:%d"%(i,staff[i])