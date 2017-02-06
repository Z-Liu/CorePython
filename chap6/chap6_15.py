#coding=utf-8
'''
Created on 2016��11��27��

@author: zhao
'''
from datetime import date
def convert_days(a_date):#DD/MM/YYYY
    return date(int(a_date[-4:]),int(a_date[3:5]),int(a_date[:2]))
    
    
def func(date1, date2):
    return (convert_days(date1)-convert_days(date2)).days

def alive_date(a_date):
    return (date.today()-convert_days(a_date)).days, (date(date.today().year, int(a_date[3:5]),int(a_date[:2]))-date.today()).days

if __name__ == '__main__':
    date1=raw_input("enter date1 DD/MM/YYYY")
    date2=raw_input("enter date2 DD/MM/YYYY")
    a_date=raw_input("enter the birthday")
    print func(date1, date2)
    print alive_date(a_date)