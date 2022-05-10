for i in range(1, 101):
    if i % 15 == 0:
        print("BUZZFIZZ")
    elif i % 5 == 0:
        print('BUZZ')
    elif i % 3 == 0:
        print('FIZZ')
    else:
        print(i)
