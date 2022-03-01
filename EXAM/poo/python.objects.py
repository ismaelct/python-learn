#!/usr/bin/python3

class fotovalor:
    def __init__(self,brillo,exposicion,contraste,saturacion):
        self.bright = brillo
        self.exposure = exposicion
        self.contrast = contraste
        self.saturation = saturacion

    def explanation(self):
        print("JPGE=b[{}]/e[{}]/c[{}]/s[{}]".format(self.bright,self.exposure,self.contrast,self.saturation))

fdef = fotovalor("33","12","-10","60")

print("""
*[BRILLO]>\t\t\t[{}]
*[EXPOSICION]>\t\t[{}]
*[CONTRASTE]>\t\t[{}]
*[SATURACION]>\t\t[{}]
""".format(fdef.bright,fdef.exposure,fdef.contrast,fdef.saturation))

fprueba = fotovalor("10","5","10","55")

fprueba.explanation()