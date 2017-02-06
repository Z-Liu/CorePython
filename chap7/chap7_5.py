#coding=utf-8
'''
Created on 2016��12��3��

@author: zhao
'''
import datetime
import hashlib
import string
db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        for i in name:
            if i not in (string.letters + string.digits):
                prompt = 'illegal name, try another: '
                break
        continue    
        name = name.lower()
        if db.has_key(name):
            prompt = 'name taken, try another:'
            continue
        else:
            break
    pwd = hashlib.md5().update(raw_input('passwd: '))
    timestamp = datetime.now()
    db[name] = [pwd, timestamp]
    

def olduser():
    name = raw_input('login: ')
    pwd = hashlib.md5().update(raw_input('passwd: '))
    passwd = db.get(name)[0]
    timstmp = db.get(name)[1]
    if passwd == pwd:
        if (datetime.now() - timstmp) > datetime.timedelta(hours=4)
            print 'welcome back', name, "your last login time is %s" % db.get(name)[1]
        else:
            print 'welcome back', name, "you already logged in at: %s" % db.get(name)[1]
        finally:
            timestamp = datetime.now()
            db[name][1] = timestamp
    else:
        print 'login incorrect'

def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choise: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True
        
    if choice == 'q': done = True
    if choice == 'n': newuser()
    if choice == 'e': olduser()

def remove_user():
    user = raw_input('enter the user to remove')
    db.pop(user, "")
    print "done"

def display_all_user():
    return db.items()

def administration():
    while True:
        prompt = """
        (1) remove a user
        (2) display all user
        """
    choice = raw_input(prompt)
    selection = {
        "1" : remove_user
        "2" : display_all_user
    }
    return selection[choice]()
    
if __name__ == '__main__':
    showmenu()