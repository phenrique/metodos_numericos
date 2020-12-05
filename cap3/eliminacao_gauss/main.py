import numpy as np

a = np.array([[3, 2, 1, 1],
              [1, 1, 2, 2],
              [4, 3, -2, 3]])
print(a, "\n")

#m = a[i,k]/ a[k,k]

atualiza_linha = lambda linha, lpivo : linha - m * lpivo

i = 1
k = 0
while k < 2:
    while i < 4 :
        m = a[i,k]/ a[k,k]
        print(m, "\n")
        a[i,] = atualiza_linha(a[i,], a[k,])
        print(a, "\n")
        i+=1

    i = 2
    k+=1


