#makeTextFile

import os
ls = os.linesep

try:
    fname = unicode(raw_input('please enter the file name:'))
except IOError, e:
    print "ERROR:'%s' already exists" % fname, e


all = []
print "\nEnter lines('.'by itself to quit).\n"


while True:
    entry = raw_input ('>')
    if entry == '.':
        break
    else:
        all.append(entry)
 
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'