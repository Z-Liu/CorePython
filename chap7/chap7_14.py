#coding=utf-8
'''
Created on 2017��2��8��

@author: zhao
'''
from random import randrange, randint

a = {randint(1,10) for i in range(randrange(9))}
b = {randint(1,10) for i in range(randrange(9))}
print a
print b
error_time=0
while True:
    union = eval(raw_input("enter a|b"))
    if union != a|b:
        error_time+=1
        if error_time==3:
            print "answer:",a|b
            break
        print "try again"
    else:
        print "good!"
        break
    
error_time=0
while True:
    intersection = eval(raw_input("enter a&b")) 
    if intersection != a&b:
        error_time+=1
        if error_time==3:
            print "answer:",a&b
            break
        print "try again"
    else:
        print "good!"
        break

c = {randint(1,10) for i in range(randrange(9))}
print c
whether_subset={"yes":True,
                "no":False}
print c.issubset(a)==whether_subset[raw_input("whether c is the subset of a? yes/no")]