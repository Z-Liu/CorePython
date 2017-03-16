#coding=utf-8
'''
Created on 2017��3��14��

@author: zhao
'''
commands={"ls":"dir","cp":"copy"}
def runCommand(command):
    (commands[command])
while True:
    command=raw_input("$")
    runCommand(command)
    
    
        