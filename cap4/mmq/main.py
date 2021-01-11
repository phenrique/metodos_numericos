#import matplotlib as plt
import numpy as np

y = [.5, .6, .9, .8, 1.2, 1.5, 1.7, 2]
n = len(y)
x = np.arange(1, n + 1)

print(x, "\n")
print(y, "\n")
#print(n, "\n")

somaX  = sum(x)
somaY  = sum(y)
somaXX = sum(x*x)
somaXY = sum(x*y)

#print(somaX, "\n")
#print(somaY, "\n")
#print(somaXX, "\n")
#print(somaXY, "\n")

c = n * somaXY
d = somaX * somaY
e = n * somaXX
f = somaX * somaX

a = (c - d) / (e - f)

print(a, "\n")

b = (somaY - (a * somaX)) / n

print(b, "\n")

print("f(x) =",a,"x","+",b)
