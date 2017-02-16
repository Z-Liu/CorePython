import random
def randCent():
    return random.randint(0,100)

#to calculate the max coin number and according remainder of given cents 
def giveChange(this_cent, this_change):
    coin_num = this_cent//this_change
    remainder = this_cent%this_change
    return (coin_num, remainder)

#there is a problem in below function
def minCoins(a_cent):
    a_coin_num = 0
    a_remainder = a_cent
    for a_change in [25, 10, 5, 1, ]:
        (coin_plus, a_remainder) = giveChange(a_remainder,a_change)
        a_coin_num += coin_plus
        if a_remainder==0:
            return a_coin_num
         
def main():
    for i in range(5):
        generated_cent = randCent()
        print "%s need %s coins" % (generated_cent,minCoins(generated_cent))
 
if __name__ == '__main__':
    main() 
