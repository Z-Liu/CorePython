def even(end):
    print [i for i in range[end] if i%2==0]
def odd(end):
    print [i for i in range[end] if i%2==1]
def whether_aliquot(dividee,divider):
    if dividee%divider==0:
        return True
    else:
        return False
if __name__ == '__main__':
    dividee=float(raw_input('enter dividee'))
    divider=float(raw_input('enter divider'))
    print whether_aliquot(dividee, divider)