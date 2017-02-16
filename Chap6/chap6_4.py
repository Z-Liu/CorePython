import math
def main():
    a_list = []
    while True:
        score = raw_input("enter the score")
        if score != ".":
            a_list.append(float(score))
        else:
            break
    print math.fsum(a_list)/len(a_list)
    

if __name__=="__main__":
    main()