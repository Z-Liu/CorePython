import math
def square_measure(length):
    return math.pow( length, 2 )
def cube_measure(length):
    return math.pow( length, 3 )
def circle_measure(length):
    return math.pow( length,2 )*math.pi
def ball_measure( length ):
    return math.pow( length,3 )*math.pi*3/4
form_measure_relation={"1" : square_measure,
                       "2" : cube_measure,
                       "3" : circle_measure,
                       "4" : ball_measure
                       }
def main(form, length):
    res = form_measure_relation[form](length)
    return res
if __name__ == '__main__':
#     form = raw_input("select the form:1)%s 2)%s 3)%s 4)%s" % ("square", "cube", "circle", "ball"))
#     length = float(raw_input("enter the length"))
#     print main(form, length)
    print [main(i, j) for (i, j) in [("1", 3), ("2", 4), ("3", 3), ("4", 2)]]
