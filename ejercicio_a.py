from pieces import *
from interpreter import draw
from picture import Picture

caballo = Picture(KNIGHT)
caballo_negativo = caballo.negative()
fila1 = caballo.join(caballo_negativo)
fila2 = caballo_negativo.join(caballo)

cuadro = fila1.up(fila2)
draw(cuadro)
