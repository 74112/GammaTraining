# string_sample = 'Hello world world'
# string_sample_1 ='first letteR is lowErcase'
# string_sample_2 = ' extra whitespase string'
# string_sample_3 = 'der Fluß'

# print(string_sample_3.lower())
# print(string_sample_3.casefold())

# print(string_sample_1.capitalize()) #ставит первое слово заклавным
# print(string_sample_1.title())# стивит каждую первую букву слова заглавной
# print(string_sample_2.strip())

name = 'Sarah'
surname = "Connor"
age = 30
result = '{} {} is {} years old'
print(result.format(name, surname, age))

result = '{1} {0} is {2} years old'
print(result.format(name, surname, age))

result = '{user_name:} {user_surname:} is {user_age} years old'
print(result.format(user_name=name, user_surname=surname, user_age=age))

result= f'Hello {name} {surname}!'
print(result)