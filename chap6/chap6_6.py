#coding=utf-8
'''
Created on 2016��11��22��

@author: zhao
'''
def func(target_str):
    reversed_str=target_str[::-1]
    index1 = 0
    for i in reversed_str:
        if i==" ":
            index1 += 1 
        else:
            break
    origin_str = reversed_str[index1:][::-1]
    index2 = 0
    for i in origin_str:
        if i==" ":
            index2 +=1 
        else:
            break
    new_str = origin_str[index2:]
    return new_str
if __name__ == '__main__':
    target_str = raw_input("prompt")
    print func(target_str)