import os


def makeTextFile():
    #makeTextFile
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

def readTextFile():
    #readTextFile
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

def main():
    selection_func={
        "1" : makeTextFile,
        "2" : readTextFile
        }
    selection=raw_input("please select which function you want to use: 1) %s; 2) %s" % ("makeTextFile", "readTextFile"))
    selection_func[selection]()

if __name__=="__main__":
    main()