import random
pokemon_a = "Pikachu"
vida_pokemon_a = random.randint(75,100)
danno_pokemon_a = random.randint(5,15)
ataque_rapido = random.uniform(0.5,1.5) * danno_pokemon_a
bola_voltio = 2.5 * danno_pokemon_a
if vida_pokemon_a < 85:
    danno_pokemon_a += 5

pokemon_b = "Tortoise"
vida_pokemon_b = random.randint(75,100)
danno_pokemon_b = random.randint(5,15)
placaje = 1.1 * danno_pokemon_b
hoja_afilada = 3 * danno_pokemon_b
if vida_pokemon_b < 85:
    danno_pokemon_b += 5

i = 0
print("Va a comenzar el combate Pokemón entre {} y {}".format(pokemon_a,pokemon_b))

while (vida_pokemon_b > 0 and vida_pokemon_a > 0) and i < 5:
    i += 1
    print("Ronda {}.".format(i))

    # Turno Pikachu
    print("Turno de {}\n Vida de {} [{}]".format(pokemon_a,pokemon_a,vida_pokemon_a))

    ataque_cpu = random.randint(1,2)

    if ataque_cpu == 1:
        vida_pokemon_b = vida_pokemon_b - ataque_rapido
    else:
        vida_pokemon_b = vida_pokemon_b - bola_voltio
        autodanno_a = random.randint(2,5)
        vida_pokemon_a = vida_pokemon_a - autodanno_a
        print("{} se ha hecho {} punto(s) de daño".format(pokemon_a,autodanno_a))

    # Turno Tortoise
    print("Turno de {}\n Vida de {} [{}]".format(pokemon_b,pokemon_b,vida_pokemon_b))
    ataque_jugador = input("¿Cual Sera tu ataque?:\n"
                           "[1] Placaje \\ [2] Hoja afilada\n")

    if ataque_jugador == 1:
        vida_pokemon_a = vida_pokemon_a - placaje
    else:
        vida_pokemon_a = vida_pokemon_a - hoja_afilada
        autodanno_b = random.randint(1,7)
        vida_pokemon_b = vida_pokemon_b - autodanno_b
        print("{} se ha hecho {} punto(s) de daño".format(pokemon_b, autodanno_b))

