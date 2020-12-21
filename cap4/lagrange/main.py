#import matplotlib as plt
import numpy as np

xi = [0.9, 1, 1.1]
yi = [0.6216, 0.5403, 0.4536]
x = 1.07

#xi = [1, 3]
#yi = [2, 1]
#x = 2

# encontrando polinômios de lagrange para cada
# valor de x
P = []
prod = 1
for j in range(0, len(xi)):
    for i in range(0, len(xi)):
        if i == j:
            continue
        prod *= (x - xi[i]) / (xi[j] - xi[i]) 
    P.append(prod)
    prod = 1

print(P)

fx = 0

#função de interpolação
for i in range(0, len(xi)):
    fx += P[i]*yi[i]

print(fx)


