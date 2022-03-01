# Asistente para elegir tu nuevo movil
# Opciones:
iphone_caro = "Iphone Pro Max"
iphone_barato = "Iphone 7"
android_barato = "Redmi C9 (100€)"
android_caro = "Google Pixel (Camara)"
android_calidadprecio = "Mi XT"

print("Bienvenido al asistente, te ayudaré a elegir tu movil nuevo.\n"
      "Te voy a hacer unas preguntas.\n")

sistema = input("¿Qué Sistema Operativo prefieres? (Android | iOS).\n")
if sistema == "android" or sistema == "Android":
      precio = input("¿Tienes presupuesto? (Si | No)\n")
      if precio == "no" or precio == "No":
            print(android_barato)
      elif precio == "si" or precio == "Si":
            camara = input("¿Te importa la cámara del movil? (Si | No)\n")
            if camara == "Si" or camara == "si":
                  print(android_caro)
            elif camara == "no" or camara == "No":
                  print(android_calidadprecio)
elif sistema == "ios" or sistema == "iOS":
      precio = input("¿Tienes presupuesto? (Si | No).\n")
      if precio == "si" or precio == "Si":
            print(iphone_caro)
      elif precio == "no" or precio == "No":
            print(iphone_barato)
