import random

is_answer_right=0
target_number=random.randint(1,100)
print target_number
while is_answer_right==0:
    x=int(raw_input('input the number you guess\n'))
    print x,target_number
    if x>target_number:
        print 'bigger'        
    elif x<target_number:
        print 'smaller'
    elif x==target_number:
        print 'right!'
        is_answer_right=1
            