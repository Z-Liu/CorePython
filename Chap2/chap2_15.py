if __name__=="__main__":
    a=int(raw_input("please enter %d number"%1))
    b=int(raw_input("please enter %d number"%2))
    c=int(raw_input("please enter %d number"%3))
    if a>=b>=c:
        print a,b,c
    elif a>=c>=b:
        print a,c,b
    elif b>=a>=c:
        print b,a,c
    elif b>=c>=a:
        print b,c,a
    elif c>=a>=b:
        print c,a,b
    elif c>=b>=a:
        print c,b,a