from math import log10
from math import sin
from math import fabs
TolX = 1e-12
TolCon = 1e-12

x1 = .2
x2 = 1

#y = lambda x: x + log10(x) - (sin(x) * sin(x))
y = lambda x: (x * x) + log10(x) - sin(x)

fx1 = y(x1)
fx2 = y(x2)
a = x1
b = x2

iter = 0

if (fx1 * fx2) > 0:
    print('Założenie nie spełnione\n')
else:
    while fabs(a - b) > TolX:
        a = b
        b = x1 - fx1 * (x2 - x1) / (fx2 - fx1)
        f0 = y(b)
        iter += 1

        if fabs(f0) < TolCon:
            break
        elif fx1 * f0 < 0:
            x2 = b
            fx2 = f0
    else:
        x1 = b
        fx1 = f0
print('Wynik: ', b, '\nLiczba iteracji: ', iter, '\n')
input()