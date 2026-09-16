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

f = lambda x: ( 1 / math.sqrt(900 - x**2)) + (1 / math.sqrt(400 - x**2)) - 1/8

a = 16
b = 17
eps = 0.001

print(bissessao(f=f, a=a, b=b, eps=eps))
