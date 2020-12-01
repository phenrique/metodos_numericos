import matplotlib as plt
#import sympy as sym
#from math import *
import math as mt
from sympy import *

x, y = symbols("x y")
#f = lambda x : exp(-x) - x
f = lambda x : x**2 - 3

#print(diff(f(x), x))
#print(diff(f(x), x, 2).subs(x, .0123))

def atende_condicao_metodo(x0):
    fx = f(x0)
    f2x = diff(f(x), x, 2).subs(x, x0)

    if (fx * f2x) > 0:
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


# Passo 1
#x0 = 0.5
x0 = 1.75

while not atende_condicao_metodo(x0):
    x0 = float(input("Digite um chute válido"))

# definições das variáveis
e = 0.01
ek = 1      # valor inicial maior que erro 
x = [x0]
k = 0

print(" xk | f(x) | f'(x) | er | xk+1")
while not atende_criterio(ek , e):
    # passo 2
    fx = f(x[k])
    f1x = diff(f(y), y, 1).subs(y, x[k])

    xk = x[k] - (fx/f1x)
    x.append(xk) 

    if(x[k] == 0):    #caso xk == 0, quebra o laço
        break;

    if k > 0:
        ek = calc_erro(x[k-1], x[k])

    print(x[k]," | ",fx," | ",f1x," | ",ek, " | ", xk)
    k += 1

print("Raiz encontrada:",x[k])

