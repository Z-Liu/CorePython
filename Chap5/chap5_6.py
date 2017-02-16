from operator import * 
str_operand_relation = {'+' : add,
                        "-" : sub,
                        "*" : mul,
                        "**" : pow,
                        "/" : div,
                        "%" : mod
                        }          
def gen_oper_element( the_form_str ):
    operand_list = str_operand_relation.keys()
    for operand in operand_list:
        if operand in the_form_str:
            fir_num = float( the_form_str.split(operand)[0] )
            sec_num = float( the_form_str.split(operand)[-1] )
            the_operand =str_operand_relation[ operand ]
    return ( fir_num, sec_num, the_operand )
def main( the_form_str ):
    ( fir_num, sec_num, the_operand ) = gen_oper_element( the_form_str )
    res = the_operand( fir_num, sec_num )
    return res
if __name__ == '__main__':
#     the_form_str = raw_input("please enter the formula you want to calculate")
#     main()
    print [main(i) for i in ["3+3", "6-7", "3*5", "2**3", "3/2", "6%5"]]