#coding=utf-8
'''
Created on 2017��2��7��

@author: zhao
'''
from string import ascii_letters
a_map={}
for i in ascii_letters:
    if 65<=ord(i)<=77 or 97<=ord(i)<=109:
        a_map[i]=chr(ord(i)+13)
    else:
        a_map[i]=chr(ord(i)-13)
def crypt(a_str):
    res=""
    for i in a_str:
        if i in a_map:
            res+=a_map[i]
        else:
            res+=i
    return res

if __name__ == '__main__':
    a_str=raw_input("enter a str")
    b_str=crypt(a_str)
    print b_str
    print crypt(b_str)