def payment(amount, balance):
    item_num = 0
    print item_num, amount, balance
    while True:
        item_num += 1
        balance -= amount
        if balance > 0:
            print "%d $%f $%f" % (item_num, amount, balance)
        else:
            print "%d $%f $%f" % (item_num, amount, 0)
            break

if __name__ == '__main__':
    balance = float(raw_input("enter opening balance"))
    amount = float(raw_input("enter monthly payment"))
    payment(amount, balance)