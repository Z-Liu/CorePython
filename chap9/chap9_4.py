#coding=utf-8
'''
Created on 2017��2��14��

@author: zhao
'''
fobj=raw_input("file name?")
with open(fobj) as f:
    while True:
        try:
            selection = raw_input("press any key to continue")
            for i in range(25):
                print f.readline(),
            continue
        except KeyboardInterrupt:
            break