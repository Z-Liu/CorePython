#coding=utf-8
'''
Created on 2017��3��15��

@author: zhao
'''
class CapOpen(object):
    def __init__(self,fn,mode='r',buf=-1):
        self.file=open(fn,mode,buf)
    def __str__(self):
        return str(self.file)
    def __repr__(self):
        return 'self.file'
    def write(self,line):
        self.file.write(line.upper())
    def __getattr__(self,attr):
        return getattr(self.file,attr)
class Time60(object):
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min
    def __str__(self):
        return '%d:%d'%(self.hr,self.min)
    __repr__=__str__
    def __add__(self,other):
        return self.__class__(self.hr+other.hr,self.min+other.min)
    def __iadd__(self,other):
        self.hr+=other.hr
        self.min+=other.min
        return self