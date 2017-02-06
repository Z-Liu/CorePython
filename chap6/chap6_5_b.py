#coding=utf-8
'''
Created on 2016��11��20��

@author: zhao
'''
def whether_equal(string_a, string_b): 
    len_a = len(string_a)
    len_b = len(string_b)
#     if len_a==len_b:
#         result=[]
#         for i in range(len_a):
#             result.append(string_a[i] == string_b[i])
#         result=all(result)
#         return result
#     else:
#         return False
    return all([string_a[i].lower()==string_b[i].lower() for i in range(len_a)]) if len_a==len_b else False
if __name__ == '__main__':
    string_a = raw_input('enter string a')
    string_b = raw_input('enter string b')
    print whether_equal(string_a, string_b)


    
