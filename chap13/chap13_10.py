#coding=utf-8
'''
Created on 2017��3��13��

@author: zhao
'''
class StaQue():
    def __init__(self):
        self.staque=[]
    def shift(self):
        retval=self.staque[0]
        self.staque=self.staque[1:]
        return retval
    def unshift(self,element):
        self.staque.insert(0,element)
    def push(self,element):
        self.staque.append(element)
    def pop(self):
        return self.staque.pop()

test=StaQue()
test.unshift(3)
test.push(5)
print test.shift()
test.unshift(6)
print test.pop()
print test.shift()