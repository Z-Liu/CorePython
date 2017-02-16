tax_percent = 0.06
def tax(amount):
    return amount*tax_percent
if __name__ == '__main__':
    print [tax(i) for i in [100, 220, 333]]