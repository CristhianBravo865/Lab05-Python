from pieces import *
from interpreter import draw
from picture import Picture

#Piezas
cuadrante = Picture(SQUARE)
torre = Picture(ROCK)
alfil = Picture(BISHOP)
caballo = Picture(KNIGHT)
rey = Picture(KING)
reina = Picture(QUEEN)
peon=Picture(PAWN)

#Lista de piezas para la fila
piezas = [torre, caballo, alfil, reina, rey, alfil, caballo, torre]

#Crear fila de fichas blancas
fila_blanca = piezas[0]
for i in range(1, len(piezas)):
    fila_blanca = fila_blanca.join(piezas[i])
#Crear fila de fichas negras
fila_negra=piezas[0].negative()
for i in range(1, len(piezas)):
    fila_negra = fila_negra.join(piezas[i].negative())

#Crear fila de peones blancos
fila_peones_blancos=peon
for i in range(1,8):
    fila_peones_blancos=fila_peones_blancos.join(peon)
#Crear fila de peones negros
fila_peones_negros=peon.negative()
for i in range(1,8):
    fila_peones_negros=fila_peones_negros.join(peon.negative())

# Crear las filas del tablero
fila1c = (cuadrante.join(cuadrante.negative())).horizontalRepeat(4)
fila2c = (cuadrante.negative().join(cuadrante)).horizontalRepeat(4)

# Superponer fila de piezas sobre la fila de cuadrados
fila_blanca_completa = fila2c.under(fila_blanca)
fila_negra_completa = fila1c.under(fila_negra)

#Superponer fila de peones 
fila_blanca_peones = fila1c.under(fila_peones_blancos)
fila_negra_peones = fila2c.under(fila_peones_negros)

tablero = fila_blanca_completa.up(fila_blanca_peones.up((fila2c.up(fila1c)).verticalRepeat(2)).up(fila_negra_peones).up(fila_negra_completa))
# Mostrar el resultado
draw(tablero)
