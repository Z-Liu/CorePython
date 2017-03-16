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
    def writelines(self,lines,newline=False):
        if newline==False:
            self.file.writelines(lines.upper())
        else:
            for line in lines:
                self.write(line+"\n")