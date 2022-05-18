import matplotlib.pyplot as plt
import  numpy as np
def f(X, x, a):
    n = len(x)
    f = 0
    for i in range(n):
        tmpf = a[i]
        for j in range(n):
            if j != i:
                tmpf *= (X - x[j])
        f += tmpf
    return f


#punkty z instukcji
x = [10, 20, 30, 40, 50]
y = [.98, .93, .86, .76, 0.64]

#punkty z przykladu
#x = [0, 1, 2, 3]
#y = [-1, 1, 5, 17]

n = len(x)
fi = np.zeros(n)
a = np.zeros(n)

for i in range(n):
    fi[i] = 1
    for j in range(n):
        if j != i:
             fi[i] = fi[i]*(x[i] - x[j])
    a[i] = y[i] / fi[i]

#zakres można dobrać dowolnie
zakres = 100
#zakres = 8; #dla punktów z przykładu
X = np.arange((-1 / 2) * zakres, zakres, .5)
Y = np.zeros(len(X))
for i in range(len(X)):
    Y[i] = f(X[i], x, a)

plt.figure(1)
plt.grid(True)
plt.title("własna implementacja")
plt.plot(X, Y, 'b-')
plt.plot(x, y, 'r*')
plt.legend(['zinterpolowana funkcja', 'dane punkty funkcji'])

#gotowa funkcja
np.polyfit(X, Y, n)
plt.figure(2)
plt.grid(True)
plt.title("gotowa funkcja")
plt.plot(X, Y, 'b-')
plt.plot(x, y, 'r*')
plt.legend(['zinterpolowana funkcja', 'dane punkty funkcji'])

plt.show()

