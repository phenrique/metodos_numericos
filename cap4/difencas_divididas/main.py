#import matplotlib as plt
import numpy as np

xi = np.array([.3, 1.5, 2.1])
yi = np.array([3.09, 17.25, 25.41] )
#xi = np.array([-1, 0, 1, 3])
#yi = np.array([3, 1, 3, 43] )

def df(x, y):
    df = []
    for i in range(1, len(x)):
        df.append((y[i] - y[i-1]) / (x[i] - x[i-1]))
    return np.array(df)

def d2f(x, y):
    df1 = df(x, y)
    d2f = []
    for i in range(1, len(df1)):
        d2f.append((df1[i] - df1[i-1]) / (x[i+1] - x[i-1]))
    return np.array(d2f)

def d3f(x, y):
    d2f1 = d2f(x, y)
    d3f = []
    for i in range(1, len(d2f1)):
        d3f.append((d2f1[i] - d2f1[i-1]) / (x[i+2] - x[i-1]))
    return np.array(d3f)

print(df(xi, yi))
print(d2f(xi, yi))
#print(d3f(xi, yi))

def f(x):
    d1fx = df(xi, yi)
    d2fx = d2f(xi, yi)
    #d3fx = d3f(xi, yi)
    soma = yi[0]
    soma += d1fx[0] * (x-xi[0])
    soma += d2fx[0] * (x-xi[0])*(x-xi[1])
    #soma += d3fx[0] * (x-xi[0])*(x-xi[1])*(x-xi[2])   
    return soma

print(f(0.4))
