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
