a = int(input('Введите длину'))
b = int(input('Введите длину'))
c = int(input('Введите длину'))
if a+b<=c or b+c<=a or a+c<=b:
    print('Треугольник не существует')
elif a!=b or a!=c or c!=b:
    print('Треугольник разностороний')
elif a==b or a==c or b==c:
    print('Треугольник равноcторнний')
else : 
    print ('Треугольник равнобедренный')
    