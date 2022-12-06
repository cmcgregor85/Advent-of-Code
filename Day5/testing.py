check = [['a'],['b']]
print(len(check))
z=check[0].pop()
print(len(check))
print(check)
if len(check)==0:
    check.append('placeholder')
    print(check)
    print(len(check))