for i in range(1, 101):
    if i % 15 == 0:
        print("BUZZFIZZ")
    elif i % 5 == 0:
        print('BAZ')
    elif i % 3 == 0:
        print('FIZZ')
    else:
        print(i)

# years
current_year = 2022
year_of_birth = 1988

current_age = abs(year_of_birth - current_year)

# name
code_1 = '354'
code_3 = 132

user_name = 'John'
user_surname = 'Smith'

# code 2 data
x = 152
y = 132
ostatok = x % y
_um_na_13 = ostatok * 13
korenj = _um_na_13 ** 0.5
tselaja_4ast = int(korenj)
otdeljnaja_peremennaja = [code_1, tselaja_4ast, code_3]

print('Hello ' + user_name + ' ' + user_surname + '. You are', current_age,
      'old. Your secret code is ' + str(otdeljnaja_peremennaja[0]) + '-' + str(otdeljnaja_peremennaja[1]) + '-' + str(otdeljnaja_peremennaja[2]) + '.')
