def profit(rate):
    return (1+rate)**365-1
if __name__ == '__main__':
    rate=float(raw_input("enter the rate\n"))
    print "annual retrun is %f" % profit(rate)