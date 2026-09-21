import math

def secante(f, x0, x1, eps_1, eps_2, kmax=100):
    for k in range(kmax):

        x2 = x1-(f(x1) / (f(x1) - f(x0))) * (x1 - x0)

        if abs(f(x2)) < eps_1 or abs(x2 - x1) < eps_2:
            return x2, k
        x0, x1 = x1, x2
    return x2


