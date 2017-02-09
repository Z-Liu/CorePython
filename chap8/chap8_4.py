#coding=utf-8
'''
Created on 2017��2��8��

@author: zhao
'''
def isprime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

if __name__ == '__main__':
    number=int(raw_input("enter number"))
    print isprime(number)
