#!/usr/bin/python3

class foto:
    brillo = 50
    exposicion = 50
    contraste = 10
    saturacion = -10

print("brillo "+str(foto.brillo) \
      +"\nexposicion "+str(foto.exposicion) \
      +"\ncontraste "+str(foto.contraste)\
      +"\nsaturacion "+str(foto.saturacion))

class foto2:
    def __init__(self,brillo,exposicion,contraste,saturacion):
        self.bright = brillo
        self.exposure = exposicion
        self.contrast = contraste
        self.saturation = saturacion

    def explanation(self):
        print("JPGE=b[{}]/e[{}]/c[{}]/s[{}]".format(self.bright,self.exposure,self.contrast,self.saturation))

fprueba = foto2("10","5","10","55")

fprueba.explanation()