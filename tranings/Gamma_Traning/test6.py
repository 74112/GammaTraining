kortez_1 = (1, 2, 32, 6565)
kortez_2 = (15, 211.2)
print(kortez_1)
kortez_1 = list(kortez_1[:2]) + list(kortez_2) + list(kortez_1[2:])

kortez_1 = tuple(kortez_1)
print(type(kortez_1))
print(kortez_1)
