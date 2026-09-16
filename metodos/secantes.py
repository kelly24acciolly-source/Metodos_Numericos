import math

def secante(f, x0, x1, eps_1, eps_2, kmax=100):
    for k in range(kmax):

        x2 = x1-(f(x1) / (f(x1) - f(x0))) * (x1 - x0)

        if abs(f(x2)) < eps_1 or abs(x2 - x1) < eps_2:
            return x2, k
        x0, x1 = x1, x2
    return x2

f = lambda x: ( 1 / math.sqrt(900 - x**2)) + (1 / math.sqrt(400 - x**2)) - 1/8

x0 = 16
x1 = 17

eps_1 = 0.001
eps_2 = 0.001

print(secante(f=f, x0=x0, x1=x1, eps_1=eps_1, eps_2=eps_2))
