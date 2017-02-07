#coding=utf-8
'''
Created on 2017��2��7��

@author: zhao
'''
from string import lower
def tr(srcstr, dststr, string, capitalization=False):
    map={}
    for i in range(len(srcstr)):
        try:
            map[srcstr[i]] = dststr[i]
        except:
            map[srcstr[i]] = ""
    res=[]
    if capitalization==False:
        for i in string:
            if lower(i) in srcstr:
                res.append(map[lower(i)])
            else:
                res.append(i)
    else:
        for i in string:
            if i in srcstr:
                res.append(map[i])
            else:
                res.append(i)
    return "".join(res)

if __name__ == '__main__':
    a_str = raw_input('srcstr, dststr, string')
    srcstr, dststr, string = tuple(a_str.split(","))
    print tr(srcstr, dststr, string)