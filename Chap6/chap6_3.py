a_list = []
selection = ''
while True:
    key_in = raw_input('key in some numbers("." to end entering)')
    if key_in != ".":
        a_list.append(key_in)
    else:
        break
print "num ordr:", sorted(a_list, key = int)
print "str order", sorted(a_list, key = str)