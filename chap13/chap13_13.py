#coding=utf-8
'''
Created on 2017��3��14��

@author: zhao
'''
class Stock(object):
    def __init__(self,name,tickerSymbol,purchaseDate,purchasePrice,numberOfShares):
        self.name=name
        self.tickerSymbol=tickerSymbol
        self.purchaseDate=purchaseDate
        self.purchasePrice=purchasePrice
        self.numberOfShares=numberOfShares
class StockPortFolio(object):
    def __init__(self):
        self.portfolio={}
    def add(self,stock):
        self.portfolio[stock.tickerSymbol]=stock
    def remove(self,stock):
        del self.portfolio[stock.tickerSymbol]
    def YTD(self,price):
        
        