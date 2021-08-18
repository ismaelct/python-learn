# Fahrenheit >> Celsius
# se utiliza float porque hay numeros decimales
grfah = float(input("Grados Fª: "))
grcel = (grfah - 32) * 5/9
print("Equivale a: {}ºC".format(grcel))
# Libras a Euros
currlib = float(input("Libras: "))
curreur = (currlib * 1.15)
print("Equivale a: {}€".format(curreur))