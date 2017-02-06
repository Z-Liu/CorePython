def func(int):
    factor1=str(int)
    ten ={
    "1":"ten",
    "2":"twenty",
    "3":"thirty",
    "4":"forty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety",
    "0":""
    }
    hundred = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":""
     }
    
    factor = factor1[::-1]
    if len(factor)==3:
        english_text ="{} {} {}".format(hundred[factor[2]]+" hundred and",ten[factor[1]],hundred[factor[0]])
    elif len(factor)==2:
        english_text ="{} {}".format(ten[factor[1]],hundred[factor[0]])
    else:
        english_text ="{}".format(hundred[factor[0]])
    return factor1, english_text
    
if __name__ == '__main__':
    a = raw_input("enter the value")
    print func(a)