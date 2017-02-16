import os
from __builtin__ import str

ls = os.linesep

def makeTextFile():
    #makeTextFile
    
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
            
def editExistedTextfile():
    while True:
        target_file=raw_input("please enter the file name")
        if os.path.exists(target_file):
            break
        else:
            pass
    list_to_write=[]
    while True:
        new_line=raw_input("please enter a new line\n'.' to exit")
        if new_line==".":
            break
        else:
            list_to_write.append(new_line)
    whether_save=raw_input("please select whether you truely want to write over the file: %s%s"%("1)yes", "2)no"))
    if whether_save.lower()=="y":
        file_handle=open(target_file,"w")
        file_handle.writelines(["%s%s"%(x, ls) for x in list_to_write])
        print "save succeeded"
    else:
        quit()
    
            

def main():
    selection_func={
        "1" : makeTextFile,
        "2" : readTextFile,
        "3" : editExistedTextfile
        }
    selection=raw_input("please select which function you want to use: 1) %s; 2) %s; 3) %s" % ("makeTextFile", "readTextFile", "editExistedTextfile"))
    selection_func[selection]()

if __name__=="__main__":
    main()