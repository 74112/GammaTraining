## from string import printable

##for B1 in printable:
##   for B3 in printable:
##        for B4 in printable:
##            print(B1, B3, B4)

for i in range(1,10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j, end=' ')
    print()
