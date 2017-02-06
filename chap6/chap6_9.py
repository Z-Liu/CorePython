def func(minutes):
    hours, minutes_remain = divmod(minutes, 60)
    return hours, minutes_remain
if __name__ == '__main__':
    minutes = int(raw_input("enter")) 
    print "time is %02d:%02d"%func(minutes)