import numpy as np

a = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]])

b = np.array([7, -8, 6])

#a = np.array([[4, -2, 1],
#              [1, -4, 1],
#              [1, 2, 4]])
#
#b = np.array([3, -2, 7])
X = np.zeros(3, dtype = int)
print(X, "\n")

U = np.triu(a,1)
L = np.tril(a,-1)
D = np.diag(np.diag(a))
inv_D = np.linalg.inv(D)

G =  L + U
print(G, "\n")
F = G.dot(inv_D)
B = b.dot(inv_D)

#B = b.dot(inv_D)

for i in range(0, 3):
    X = X.dot(F)  + B 
    print(X, "\n")

#print(a, "\n")
#print(U, "\n")
#print(L, "\n")
#print(D, "\n")
#print(inv_D, "\n")
#print(F, "\n")
#print(B, "\n")
#print(x1, "\n")
#print(x2, "\n")



#print(b, "\n")
##print(F, "\n")
##print(D, "\n")
#print(X, "\n")

