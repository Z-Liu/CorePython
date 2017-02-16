from numpy import average

def enter_the_numbers():
    list_to_operate=[]
    for i in range(5):
        number_to_append=float(raw_input("please the %s number"%(i+1)))  
        list_to_operate.append(number_to_append)
    return list_to_operate

def sum_the_numbers():
    list_to_sum=enter_the_numbers()
    sum_result=sum(list_to_sum)
    return sum_result

def average_the_numbers():
    list_to_average=enter_the_numbers()
    average_result=sum(list_to_average)/5
    return average_result

if __name__=="__main__":
    while True:
        print"(1)sum\n(2)average\n(3)exit"
        selection=raw_input('please enter your selection')
        if selection=="1":
            result_to_render=sum_the_numbers()
            print result_to_render
        elif selection=="2":
            result_to_render=average_the_numbers()
            print result_to_render
        elif selection=="3":
            break                
    quit()   
    