#coding=utf-8
'''
Created on 2017��2��6��

@author: zhao
'''
from string import split

data=[]
while True:
    column_string = raw_input("please enter 'stock ticker symbol, number of shares, purchase price,"+\
    " current price'")
    if column_string:
        data.append(split(column_string,","))
    else:
        break
selection = int(raw_input("select one field as key. 1)stock ticker symbol 2)number of shares 3)purchase price "+\
    "4)current price"))-1
all_row={}
for i in data:
    key = i.pop(selection) 
    all_row[key] = i
print all_row


    
