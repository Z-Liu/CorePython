#coding=utf-8
'''
Created on 2017��2��28��

@author: zhao
'''
j,k=1,2
def proc1():
    j,k=3,4
    print "j==%d and k==%d"%(j,k)
    k=5
def proc2():
    global j
    j=6
    proc1()
    print "j==%d and k==%d"%(j,k)
k=7
proc1()
print "j==%d and k==%d"%(j,k)

j=8
proc2()
print "j==%d and k==%d"%(j,k)
#3,4
#1,7
#3,4
#6,7
#8,7 #6,7