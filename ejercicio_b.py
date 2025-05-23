from pieces import *
from interpreter import draw
from picture import Picture

caballo = Picture(KNIGHT)
caballo_negativo = caballo.negative()
fila1 = caballo.join(caballo_negativo)
fila2 = caballo_negativo.verticalMirror().join(caballo.verticalMirror())  

cuadro = fila2.up(fila1)
draw(cuadro)
