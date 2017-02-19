#coding=utf-8
'''
Created on 2017年2月16日

@author: zhao
'''
def tax(amount,tax_rate=0.06):
    return amount*tax_rate
print tax(100)
print tax(200,0.1)