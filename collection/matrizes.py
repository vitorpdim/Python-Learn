import numpy as np

matriz = np.array([[2, 3, 3], 
                   [4, 5, 7]])

matriz.shape # retorna quantidade de linhas e colunas espcificas
print(matriz)

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range (matriz.shape[1]):
        print (matriz[1][1])