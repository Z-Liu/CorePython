def greatest_common_divisor(num1, num2):
    print "caculating greatest_common_divisor"
    res = max(num1, num2)
    while not(num1 % res == 0 and num2 % res == 0):
        res-=1
    return res

def least_common_multipe(num1, num2):
    print "caculating least_common_multiple"
    res = 1
    while not(res % num1 == 0 and res % num2 == 0):
        res += 1
    return res

selection_map={"1" : greatest_common_divisor,
           "2" : least_common_multipe
           }

if __name__ == '__main__':
    selection = raw_input("select which to calculate: 1) %s 2) %s\n" % ("greatest_common_divisor", "least_common_multipe"))
    num1_str, num2_str = raw_input("enter '%s , %s'\n" % ("num1", "num2")).split(",")
    num1, num2 = int(num1_str), int(num2_str)
    print selection_map[selection](num1, num2)