#coding=utf-8
'''
Created on 2016Äê12ÔÂ3ÈÕ

@author: zhao
'''
def func(list1, list2):
    return dict(zip(list1, list2))

if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    list2 = [12340,52830574,1726342,2834982,8234]
    print func(list1, list2)