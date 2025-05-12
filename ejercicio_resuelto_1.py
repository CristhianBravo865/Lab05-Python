def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    return False
            elif m[i][j] != d:
                return False
    return True

#Matriz escalar
matriz1 = [
    [3, 0, 0],
    [0, 3, 0],
    [0, 0, 3]
]
#Matriz no escalar
matriz2 = [
    [2, 0, 1],
    [0, 2, 0],
    [0, 0, 2]
]

#print(esEscalar(matriz1))  # Verdadero
#print(esEscalar(matriz2))  # Falso
