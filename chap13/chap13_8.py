#coding=utf-8
'''
Created on 2017��3��9��

@author: zhao
'''
class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def isempty(self):
        return len(self.stack)==0
    def peek(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return None

test=Stack()
test.push(3)
print test.isempty()
print test
print test.peek()
print test.pop()
print test.peek()
print test.isempty()

        