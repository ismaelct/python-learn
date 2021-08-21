# Fahrenheit >> Celsius
# se utiliza float porque hay numeros decimales
grados_f = float(input("Grados Fª: "))
grados_c = (grados_f - 32) * 5/9
print("Equivale a: {}ºC".format(grados_c))
# Libras a Euros
libras = float(input("Libras: "))
euros = (libras * 1.15)
print("Equivale a: {}€".format(euros))