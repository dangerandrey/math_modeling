print ('Введите коэффиценты:')
a = float(input('a = ' ))
b = float(input('b = ' ))
c = float(input('c = ' ))
D = b**2-4*a*c;
print(D)
if D > 0:
    x1 = (-b + D**(1/2)) / (2 * a)
    x2 = (-b - D**(1/2)) / (2 * a)
    print(x1,x2)
elif D== 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Корней нет')