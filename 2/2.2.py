import math
t = float(input("Введите t -"))
a = t - 2
b = 4*t -1
c = 3*t - 5
discr = b**2 - 4 *a*c
print("Дискриминант D = ", discr)
if a == 0:
    print("Линейное уравнение")
    l = b/c
    print(l)
elif discr > 0:
    x1 = (-b + math.sqrt(discr))/(2*a)
    x2 = (-b - math.sqrt(discr))/(2*a)
    print(x1,x2)
elif discr == 0:
    x = -b/(2*a)
    print("x=", x)
else:
    print('корней нет')
