import numpy as np
from scipy import linalg

def calc_erro(x0, x1):
    return  abs(x1-x0)

def atende_criterio(ek, e):
    if ek <= e:
        return True
    else:
        return False

#a = np.array([[3, -.1, -.2],
#              [.1, 7, -.3],
#              [.3, -.2, 10]])
#
#b = np.array([7.85, -19.3, 71.4])

a = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]])

b = np.array([7, -8, 6])

# Matriz de termos independentes
#a = np.array([[4, -2, 1],
#              [1, -4, 1],
#              [1, 2, 4]])
#
## Matriz de termos independentes
#b = np.array([3, -2, 7])

# Vetor de solução
X = np.zeros(3, dtype = int)

#Matrix triangular superior
U = np.triu(a,1)

#Matrix triangular inferior
L = np.tril(a,-1)

#Matrix Diagonal
D = np.diag(np.diag(a))

#Matrix Diagonal inversa
inv_D = np.linalg.inv(D)

G = D + L 
#print(G, "\n")

inv_G = np.linalg.inv(G)
#print(inv_G, "\n")

F = np.dot(inv_G, U)
#print(F, "\n")
F = F*(-1)
B = np.dot(inv_G, b)
#print(B, "\n")

e = 0.05
ek = np.ones(3)
i = 0

while not atende_criterio(max(ek), e):
    Xk = F.dot(X)  + B 
    ek = calc_erro(X, Xk)# Vetor de erros
    X = Xk
    i = i + 1
    print(i,"º interação: ",X, "\n")
