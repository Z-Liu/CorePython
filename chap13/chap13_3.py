#coding=utf-8
'''
Created on 2017��3��1��

@author: zhao
'''
def dollarize(floatingValue):
    roundFloat=round(floatingValue,2)
    if roundFloat<0:
        return"-${:,}".format(-roundFloat)
    return "${:,}".format(roundFloat)

class MoneyFmt(object):
    def __init__(self,value=0.0,theFormat="sign"):
        self.value=float(value)
        self.theFormat=theFormat
    def update(self,value=None):
        self.value=float(value)
    def __repr__(self):
        return repr(self.value)
    def __str__(self):
        formatStr="${:,.2f}"
        if self.value<0:
            if self.theFormat=="sign":
                return ("-"+formatStr).format(-self.value)
            else:
                return ("("+formatStr+")").format(-self.value)
        else:
            return formatStr.format(self.value)
    def __nonzero__(self):
        if self.value>0:
            return True
        return False
cash=MoneyFmt(123.45)
print repr(cash)
print cash
cash.update(10000.4567)
print repr(cash)
print cash
cash.update(-0.3)
print repr(cash)
print cash
print repr(str(cash))