vvod = [float(input('Enter A:')), float(input('Enter B:')), float(input('Enter C:'))]

if vvod[2] ** 2 == vvod[0] ** 2 + vvod[1] ** 2:

    print('Треугольник со сторонами :', vvod[0], " ", vvod[1], " ", vvod[2], ', является прямоугольным')
else:
    print('Треугольник со сторонами :', vvod[0], " ", vvod[1], " ", vvod[2], ', не является прямоугольным')
