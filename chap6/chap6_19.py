#coding=utf-8
'''
Created on 2016��11��29��

@author: zhao
'''
def func(a_sequence, columns, direction="horizontal"):
    rows, remainder_len = divmod(len(a_sequence), columns)
    if direction == "horizontal":
        for i in range(rows):
            for j in range(columns):
                print a_sequence.pop(0),
            print
        for i in range(columns-remainder_len):
            print " ",
        for i in range(remainder_len):
            print a_sequence.pop(0)
    elif direction == "vertical":
        rows ,columns = columns, rows
        for i in range(rows):
            for j in range(columns):
                print a_sequence[j*rows+i],
            print
        for i in range(columns-remainder_len):
            print " ",
        for i in range(remainder_len):
            print a_sequence[columns*rows+i],

if __name__ == '__main__':
    a_sequence, columns, direction = [1,2,3,4,5,6,7,8,9,10,11], 3, "vertical"
    func(a_sequence, columns, direction)