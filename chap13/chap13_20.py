#encoding=utf-8
'''
Created on 2017��3��21��

@author: Administrator
'''
class Time60(object):
    def __init__(self,*args,**kwargs):
        if args==() and kwargs=={}:
            self.hr=0
            self.min=0
        elif len(args)==2:
            self.hr=args[0]
            self.min=args[1]
        elif kwargs!={}:
            self.hr=kwargs['hr']
            self.min=kwargs['min']
        elif isinstance(args[0],dict):
            self.hr=args[0]['hr']
            self.min=args[0]['min']
        elif isinstance(args[0],str):
            hourAndMin=args[0].split(":")
            self.hr=int(hourAndMin[0])
            self.min=int(hourAndMin[1])
    def __str__(self):
        return '%02d:%02d'%(self.hr,self.min)
    def __add__(self,other):
        hrPlus,minRemain=divmod((self.min+other.min), 60)
        return self.__class__(self.hr+other.hr+hrPlus,minRemain)
    def __iadd__(self,other):
        self.hr+=other.hr
        self.min+=other.min
        return self
    def __sub__(self,other):
        hrPlus,minRemain=divmod((self.min+other.min), 60)
        return self.__class__(self.hr-other.hr+hrPlus,minRemain)
    def __isub__(self,other):
        hrPlus,minRemain=divmod((self.min+other.min), 60)
        self.hr-=other.hr
        self.hr+=hrPlus
        self.min=minRemain
        return self
    def __repr__(self):
        return "Time60('%02d:%02d')"%(self.hr,self.min)
    def __int__(self):
        return self.hr*60+self.min


# a = Time60()
# print a
# a = Time60(12, 1)
# print a
# a = Time60({'hr':12,'min':2})
# print a
# a = Time60("12:3")  
# print a
# a = Time60(hr=12,min=4)
# print a
# print repr(a)
thu=Time60(10,30)
fri=Time60(8,45)
print thu+fri