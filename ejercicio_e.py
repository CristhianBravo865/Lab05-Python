from pieces import *
from interpreter import draw
from picture import Picture
cuadrante = Picture(SQUARE)
draw((cuadrante.negative().join(cuadrante)).horizontalRepeat(4))
