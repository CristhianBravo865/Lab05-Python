from ejercicio_resuelto_1 import esEscalar
def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)

#Matriz unitaria
matriz1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

#Matriz no unitaria
matriz2 = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
]

print(esUnitaria(matriz1))  # V
print(esUnitaria(matriz2))  # F