# def square(x):
#    print(x**2)
#    return (x**2)

# a=square(12)

# print(a)
def test(x):
    if x % 2 == 0:
        return True

for i in range(1, 25):
    print(i, test(i))
