#coding=utf-8
'''
Created on 2016��11��26��

@author: zhao
'''
def func(a_string):
    from string import ascii_lowercase, ascii_uppercase
    lower_to_upper = {ascii_lowercase[i] : ascii_uppercase[i] for i in range(len(ascii_uppercase))}
    upper_to_lower = {ascii_uppercase[i] : ascii_lowercase[i] for i in range(len(ascii_uppercase))}
    new_string = ""
    for i in a_string:
        if i in ascii_lowercase:
            new_string+=lower_to_upper[i]
        elif i in ascii_uppercase:
            new_string+=upper_to_lower[i]
        else:
            new_string+=i
    return new_string
if __name__ == '__main__':
    a_string = raw_input('prompt')
    print func(a_string)