import math
x = 1
y = 2
z = 2
r = (z**2 * x**2) - (3**x * y**z) - math.exp(math.sin(x)+4)
print(r)

import math
x = 3
r = 2*math.cos(x/2)**2 - math.log(abs(x/2))**2
print(r)

import math
x = 0.1
y = 3
r = (x/(5*y)) - ((math.log(2 - math.exp(x)))/3 + x - 3*y)
print(r)

import math
x = 0.3
A = x + math.sqrt(x**2 + 1)**1/2
B = math.asin(3*x) - 0.6
r = (A / B)**(1/3)
print(r)

B ЧАСТЬ 
import math
g = 0
h = 0
x = g + h
t = math.log(math.cos(x) ** 2)
r = (((math.sin(x))**4 + 8)**(1/2) + 4)/(7*x*t + 1)
print (r)
