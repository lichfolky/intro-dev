import random
import librerie.my_random as rng

bicchieri = [True, False, False]
print(bicchieri)
rng.shuffle(bicchieri, 5)

## qui chiamo la funzione shuffle della libreria random
# print(random.shuffle(bicchieri))
print(bicchieri)

bicchiere_scelto = int(input("scegli un bicchiere ")) - 1
print(bicchieri[bicchiere_scelto])
