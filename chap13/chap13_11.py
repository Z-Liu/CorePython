#coding=utf-8
'''
Created on 2017Äê3ÔÂ13ÈÕ

@author: zhao
'''
class User(object):
    def __init__(self):
        self.carts=[]
    def add(self):
        self.carts.append(Cart())
    def delete(self,cartNo):
        self.carts.remove(cartNo)
        
class Cart(object):
    def __init__(self):
        self.items=[]
    def add(self,name,price):
        self.items.append(Item(name,price))
    def delete(self,itemNo):
        self.items.remove(itemNo)

class Item(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price