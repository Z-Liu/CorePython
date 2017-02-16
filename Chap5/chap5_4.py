def bissextileYear(this_year):
    condition1=bool( this_year%4==0 )and bool( this_year%100!=0 )
    condition2=bool( this_year%400==0 )
    if condition1 or condition2:
        print "this is a bissextile year"
    else:
        print "this is not a bissextile year"
def main():
    while True:
        a_year=int(raw_input("enter a year"))
        bissextileYear(a_year)
if __name__ == '__main__':
    main()
        
    
    