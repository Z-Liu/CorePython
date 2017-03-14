#coding=utf-8
'''
Created on 2017��3��13��

@author: zhao
'''
class Queue(object):
    def __init__(self):
        self.queue=[]
    def enqueue(self,element):
        self.queue.insert(0, element)
    def dequeue(self):
        return self.queue.pop()

test=Queue()
test.enqueue(3)
test.enqueue(5)
print test.dequeue()
print test.dequeue()