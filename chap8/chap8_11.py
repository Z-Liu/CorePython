#coding=utf-8
'''
Created on 2017��2��10��

@author: zhao
'''
import re
name_list=[]
name_list_max_len=5
wrong_times=0
prog = re.compile(".+\,.+")
while len(name_list) < name_list_max_len:
    name = raw_input("enter name"+str((len(name_list)+1)))
    if not prog.match(name):
        print "wrong format"+str(wrong_times+1)+"time(s)"
        continue
        wrong_times+=1
    else:
        print "right format"
        name_list.append(name)
        continue
for i in sorted(name_list):
    print i