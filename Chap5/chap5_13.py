def time_str_to_number(string):
    (hour, minute) = [int(i) for i in string.split(":")]
    return (hour, minute)
def time_tranlate(string):
    (hour, minute) = time_str_to_number(string)
    return hour*60+minute
if __name__ == '__main__':
    string = raw_input("enter time %s:%s\n"%("HH", "MM"))
    print time_tranlate(string)