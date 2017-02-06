#coding=utf-8
'''
Created on 2016��11��27��

@author: zhao
'''
def conversion(string):
    pos=max(string.rfind("+"), string.rfind("-"))
    if "j" in string:
        real=float(string[:pos])
        imag=float(string[pos:-1])
    else:
        real=float(string)
        imag=0
    return complex(real, imag)

if __name__ == '__main__':
    string=raw_input("enter")
    print conversion(string)