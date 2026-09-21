import math

def bissessao(f, a, b, eps, k_max=100):
    k = 0
    while k < k_max:
        x = (a + b) / 2
        fx = f(x)

        if abs(fx) < eps or (b - a) / 2 < eps:
            return x, k + 1
        
        if f(a) * fx < 0:
            b = x
        else:
            a = x

        k = k + 1

    return x, k


