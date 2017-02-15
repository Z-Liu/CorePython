#coding=utf-8
'''
Created on 2017��2��14��

@author: zhao
'''
def grade(score):
    return score
    pass
filelist=[]
while True:
    fobj=raw_input('enter file name, "." to terminate')
    if fobj!=".":
        filelist.append(fobj)
        continue
    else:
        break
scores=[]
for i in filelist:
    with open(i) as f:
        for j in f:
            scores.append(j)
for score in scores:
    print grade(score),
        
    