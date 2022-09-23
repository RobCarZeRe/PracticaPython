#Actividad 1
import numpy as np
a = np.array([1,3,5,7]) #inicializando un vector
b = type(a)
print(b)


import numpy as np

# dimensions of the matrix
n, m = 2, 3

# create resulting matrix (init with zeros for convenience)
result = np.zeros((n, m), dtype=int)

# fill up first 2 elements of the matrix
result[0 // m][0 % m] = 0
result[1 // m][1 % m] = 1

# now you don't need to refer to the matrix but store 2 last
# fibonacci numbers
prevprev = 0
prev = 1

for i in range(2, n * m):
    current = prevprev + prev
    result[i // m][i % m] = current
    prevprev = prev
    prev = current

# print the result
print(result)