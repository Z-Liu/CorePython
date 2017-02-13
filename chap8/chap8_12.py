#coding=utf-8
'''
Created on 2017��2��10��

@author: zhao
'''
begin_value=int(raw_input("enter begin value"))
end_value=int(raw_input("enter end value"))
def print_format(value):
    print "{0:2d}".format(value), " {0:06b}".format(value),\
     " {0:2o}".format(value), " {0:2x}".format(value), chr(value)
for value in range(begin_value, end_value+1):
    print_format(value)