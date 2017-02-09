#coding=utf-8
'''
Created on 2017��2��9��

@author: zhao
'''
def getfactors(number):
    res=[]
    for i in range(1,number+1):
        if number%i==0:
            res.append(i)
    return res

if __name__ == '__main__':
    number=int(raw_input("enter number"))
    print getfactors(number)