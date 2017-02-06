#coding=utf-8
'''
Created on 2016��12��1��

@author: zhao
'''
def for_tuple(tuple):
    return tuple[1]
def func(a_dict):
    for key in sorted(a_dict.keys()):
        print key, a_dict[key]
    the_items = sorted(a_dict.items(), key=for_tuple)
    for i in the_items:
        print i
if __name__ == '__main__':
    a_dict={
        5:"a",
          1:"e",
          3:"c",
          2:"b"
        }
    
    func(a_dict)