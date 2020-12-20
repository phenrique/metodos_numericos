import matplotlib as plt
from sympy import *
#from math import *

x, y = symbols("x y")

f = lambda x : x**3 - 4*x**2 + x + 6
print('Função: x**3 - 4*x**2 + x + 6 ')

#f = lambda x : exp(-x) - x
#print('Função: exp(-x) - x')

#print(diff(f(x), x))
#plot(f(x));

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

# definições das variáveis

a = 1.4
b = 2.5
dx = 0.01

e = 0.01
ek = 1
x = []
k = 0


# Passo 1
# procura intervalo 
while not atende_bosano(f(a), f(b)):
    b += dx

print("intervalo: [",a,",",b,"]")
     


print("k | a | b | Xk | er | f(Xk)")
while not atende_criterio(ek , e):

    xk = (a*f(b) - b*f(a)) / (f(b) - f(a))
    x.append(xk) 

    if(x[k] == 0):    #caso xk == 0, quebra o laço
        break;

    # escolhe intervalo 
    if atende_bosano(f(a), f(x[k])):
        b = x[k]
    else:    
        a = x[k]

    if k > 0:
        ek = calc_erro(x[k-1], x[k])


    print(k," | ",a," | ",b," | ",x[k]," |",ek," | ",f(x[k]))
    k += 1

xk = x[k-1]
print("Raiz encontrada:",xk)

