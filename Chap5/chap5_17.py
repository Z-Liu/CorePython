import random
N = random.randint(2,100)
print N
a_list = [random.randint(0,pow(2,31)-1) for i in range(N)]
a_list = sorted(a_list)
print a_list