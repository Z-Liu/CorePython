def grade(this_score):
    if 90<=this_score<=100:
        return "A"
    elif 80<=this_score<=89:
        return "B"
    elif 70<=this_score<=79:
        return "C"
    elif 60<=this_score<=69:
        return "D"
    elif this_score<60:
        return "F"
def main():
    while True:
        keyin_score=float(raw_input("enter the score"))
        result=grade(keyin_score)
        print result
if __name__ == '__main__':
    main()