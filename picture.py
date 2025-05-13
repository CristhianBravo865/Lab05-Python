from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        nueva_imagen = []
        for fila in self.img:
            nueva_fila = ""
            for caracter in reversed(fila):
                nueva_fila += caracter
            nueva_imagen.append(nueva_fila)
        return Picture(nueva_imagen)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        nueva_imagen = []
        for i in range(len(self.img) - 1, -1, -1):
            nueva_imagen.append(self.img[i])
        return Picture(nueva_imagen)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        nueva_imagen = []
        for fila in self.img:
            nueva_fila = ""
            for caracter in fila:
                nueva_fila += self._invColor(caracter)
            nueva_imagen.append(nueva_fila)
        return Picture(nueva_imagen)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        nueva_imagen = []
        for i in range(len(self.img)):
            nueva_fila = self.img[i] + p.img[i]
            nueva_imagen.append(nueva_fila)
        return Picture(nueva_imagen)

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p debajo de la actual """
        nueva_imagen = self.img + p.img
        return Picture(nueva_imagen)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        return Picture(None)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    # Extra: Sólo para realmente viciosos 
    def rotate(self):
        """ Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario """
        return Picture(None)
