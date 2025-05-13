from pieces import *
from interpreter import draw
from picture import Picture
cuadrante = Picture(SQUARE)
draw((cuadrante.join(cuadrante.negative())).horizontalRepeat(4))
