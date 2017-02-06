#coding=utf-8
'''
Created on 2016��11��20��

@author: zhao
'''
def whether_double(string):
    string = string.translate(None, ' ')
    len_str = len(string)
    return all([string[i] == string[len_str-1-i] for i in range(len_str/2)]) if len_str%2 == 0 else False

if __name__ == '__main__':
    string = raw_input('enter string')
    print whether_double(string)