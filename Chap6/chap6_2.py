import string
import keyword

alphas = string.letters+''
nums = string.digits

print 'welcome to the identifier checkers v1.1'

myInput = raw_input('identifier to test?')

if myInput[0] not in alphas:
    print '''invalid: first symbol must be
    alphabetic'''
else:
    for otherChar in myInput[1:]:
        if otherChar not in alphas + nums:
            print '''invalid: remaining
            symbols must be alphanumeric'''
            break
        else:
            print "okay as an identifier"

if myInput in keyword.kwlist:
    print 'in kwlist'
else:
    print 'not in kwlist'