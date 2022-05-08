a = 15
b = 2
# print(a, type(a), b, type(b))
# c = a + b
# print(c, type(c))
# text = 'bugaga'

# print(str(a) + text)
# print \
#    (a / b)
##print(a // b)
print(a % b)
# _a = text[2]
# print(_a)
# asddd = None
# print(asddd)
# print("""rent""")

storon_A = float(input('Please insert side A: '))
storon_B = float(input('Please insert side B: '))
storon_C = float(input('Please insert side C: '))
poluperriment = (storon_A + storon_B + storon_C) / 2
ploshadj = (poluperriment * (poluperriment - storon_A) * (poluperriment - storon_B) * (poluperriment - storon_C)) ** 0.5
print('Прощадь треугольника: '+ str(ploshadj))
