#coding=utf-8
'''
Created on 2017��2��21��

@author: zhao
'''
def bissextileYear(this_year):
    condition1=bool( this_year%4==0 )and bool( this_year%100!=0 )
    condition2=bool( this_year%400==0 )
    if condition1 or condition2:
        return True
    else:
        return False
def filter_year(years):
    return filter(bissextileYear,years)
def list_year(years):
    return [year for year in years if bissextileYear(year)]
years=[2017,2008,2007,2000,1900]
print filter_year(years)
print list_year(years)