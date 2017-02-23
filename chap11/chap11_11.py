#coding=utf-8
'''
Created on 2017��2��21��

@author: zhao
'''
def trim(line):
    return line.strip(" ")
f=open(raw_input("enter file"))
new_lines=map(trim,f.readlines())
def newfile():
    file(f.name+"_new","w").writelines(new_lines)
def overwrite():
    file(f.name,"w").writelines(new_lines)
selection={"1":newfile,
           "2":overwrite}
mode=selection[raw_input("select which way:1.newfile 2.overwrite")]
mode()