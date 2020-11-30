import matplotlib as plt
import sympy as sym
from math import *


#x, y = sym.symbols("x y")
#sym.plot(f(x), (x, -5, 6))

# definição da função
#f = lambda x : 10*log(x) - 3*x - 1
#print('Função: 10*log(x) - 3*x - 1')

f = lambda x : exp(-x) - x

print('Função: exp(-x) - x')

def atende_bosano(fa, fb):
    if (fa * fb) < 0:
        return True
    else:
        return False

def calc_erro(x0, x1):
    return  abs(x1-x0)

def atende_criterio(ek, e):
    if ek <= e:
        return True
    else:
        return False

a = 0
b = 0
dx = 0.001

e = 0.00001
ek = 1
x = []
k = 0

# procura intervalo 
while not atende_bosano(f(a), f(b)):
    b += dx
     


print("k | a | b | Xk | er | f(Xk)")
while not atende_criterio(ek , e):

    x.append((a + b) / 2) 

    if atende_bosano(f(a), f(x[k])):
        b = x[k]
    else:    
        a = x[k]

    if k > 0:
        ek = calc_erro(x[k-1], x[k])


    print(k," | ",a," | ",b," | ",x[k]," |",ek," | ",f(x[k]))
    k += 1

