#coding=utf-8
'''
Created on 2017��3��7��

@author: zhao
'''
import math
class Point(object):
    def __init__(self,X=0,Y=0):
        self.x=X
        self.y=Y
    def __repr__(self):
        return self.x,self.y
class LineSegment(object):
    def __init__(self,x1,y1,x2,y2):
        self.point1=Point(x1,y1)
        self.point2=Point(x2,y2)
    def __repr__(self):
        return str(self.point1.__repr__())+","+str(self.point2.__repr__())
    def length(self):
        res=math.sqrt(pow(self.point1.x-self.point2.x,2)+pow(self.point1.y-self.point2.y,2))
        return res
    def slope(self):
        return abs(self.point2.y-self.point1.y)/abs(self.point2.x-self.point1.x)
test=LineSegment(0,0,1,1)
print repr(test)
print test.length()
print test.slope()
    