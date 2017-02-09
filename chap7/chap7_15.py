#coding=utf-8
'''
Created on 2017Äê2ÔÂ8ÈÕ

@author: zhao
'''
a=eval(raw_input("enter the first set"))
b=eval(raw_input("enter the second set"))
res={"&":a&b,
     "|":a|b
    }
print res[raw_input("select the operand")]