from math import log10
from math import sin
from math import fabs

TolX = 1e-12

a = 0.5
b = 1

# y = def lambda x: x + log10(x) - (sin(x) * sin(x))
y = lambda x: (x * x) + log10(x) - sin(x)

iter = 0
while fabs(a - b) > TolX:
    x1 = (a + b) / 2
    iter += 1
    if y(x1) == 0:
       break
    elif y(a) * y(x1) < 0:
        b = x1
    elif y(b) * y(x1) < 0:
        a = x1
print('Wynik:', x1, '\nLiczba iteracji: ', iter, '\n')
input()
