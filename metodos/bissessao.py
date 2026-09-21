import math

def bissessao(f, a, b, eps, k_max=100):
    k = 0
    while(b - a >= eps) and (k < k_max):
        x = (a + b) / 2

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        k = k + 1

    return (a + b) / 2, k


