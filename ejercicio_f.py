from pieces import *
from interpreter import draw
from picture import Picture
cuadrante = Picture(SQUARE)
fila1=(cuadrante.join(cuadrante.negative())).horizontalRepeat(4)
fila2=(cuadrante.negative().join(cuadrante)).horizontalRepeat(4)
draw((fila2.up(fila1)).verticalRepeat(2))