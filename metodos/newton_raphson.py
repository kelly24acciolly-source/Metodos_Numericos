import math

def newton_raphson(f, f_, x0, eps_1, eps_2, k_max=100):
    k = 0

    x = x0

    while k < k_max:
        x_novo = x - f(x) / f_(x)

        if abs(f(x_novo)) < eps_1:
            return x_novo, k+1
        if abs(x_novo - x)  < eps_2:
            return x_novo, k+1

        x = x_novo
        k = k + 1

    return x, k

f = lambda x: ( 1 / math.sqrt(900 - x**2)) + (1 / math.sqrt(400 - x**2)) - 1/8
f_ = lambda x: (x / (900 - x**2)**(3/2)) + (x / (400 - x**2)**(3/2))

x0 = 16.5

eps_1 = eps_2 = 0.001

print(newton_raphson(f=f, f_=f_, x0=x0, eps_1=eps_1, eps_2=eps_2))