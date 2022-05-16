contacts = {
    'John Kennedy': {'birthday': "29/05/1917",
                     'city': "Brookline", "Phone": None, "children": 3},
    'Arny': {'birthday': "30/06/2047", 'city': 'Gradec', "Phone": '123-45-67', "children": 5},
    'Donald': {'birthday': "15/06/1947", 'city': 'Mars', "Phone": '987-65-43', "children": 12}
}
persons = ['John Kennedy', 'Arny', 'Donald']
for person in persons:
    ## 1 й вариант обхода словаря по ключам
    birthday = contacts[person]['birthday']
    city = contacts[person]['city']
    Phone = contacts[person]['Phone']
    children = contacts[person]['children']
    print(person, birthday, city, Phone)
    ## 2 й вариант обхода словаря по ключам
print('/////////////////////////////////////////////')
for person in persons:
    print(person)
    for data in contacts[person]:
        print(data,'-', contacts[person][data])
