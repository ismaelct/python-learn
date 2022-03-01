import random
i = 0

numero = random.randint(1,20)
while numero > 1:
        print("Mi nº es mayor que 1, es {}".format(numero))
        numero = random.randint(1, 20)
        i += 1

i += 1
print("Mi nº es {} ha tardado {}".format(numero,i))