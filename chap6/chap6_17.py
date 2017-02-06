#coding=utf-8
'''
Created on 2016��11��29��

@author: zhao
'''
def myPop(a_list):
    a=a_list[-1]
    a_list.remove(a_list[-1])
    return a, a_list

if __name__ == '__main__':
    a_list = eval(raw_input("enter"))
    print myPop(a_list)