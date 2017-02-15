#coding=utf-8
'''
Created on 2017��2��14��

@author: zhao
'''
file1=raw_input("enter file1")
file2=raw_input("enter file2")
row=0
with open(file1) as f1, open(file2) as f2:
    for i in f1:
        j=f2.next()
        row+=1
        if i==j:
            continue
        else:
            print row
        column=0
        for m in range(len(i)):
            column+=1
            if i[m]!=j[m]:
                print column
                break
        break