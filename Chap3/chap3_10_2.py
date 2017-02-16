#readTextFile
import os
while True:
    fname = raw_input('Enter filename:')
    if os.path.exists(fname)==True:
        fobj = open(fname, 'r')
        for eachLine in fobj:
            print eachLine,
        fobj.close()
        break
    else:
        print '*** file open error:'
