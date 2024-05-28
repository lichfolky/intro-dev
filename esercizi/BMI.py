import math
import os
os.system('cls||clear')

"""
BMI = peso / altezza ^ 2

Sottopeso       -           BMI < 18.5  
Peso normale    -   18.5 <= BMI < 25.0  
Sovrappeso      -   25.0 <= BMI < 30.0  
Obesità         -   30.0 <= BMI
"""

peso = input("Inserisci il peso in kg ")
peso_int = int(peso)
altezza = input("Inserisci l'altezza m ")
altezza_int = float(altezza)

# str() e int(), float() servono a convertire il tipo di un valore

BMI = peso_int / math.pow(altezza_int, 2)

if BMI < 18.5:
    print("Sottopeso")
else:
    if BMI < 25:
        print("Peso normale")
    else:
        if BMI < 30:
            print("Sovrappeso")
        else:
            print("Obesità")


if BMI < 18.5:
    print("Sottopeso")

if BMI >= 18.5 and BMI < 25:
    print("Peso normale")

if BMI >= 25 and BMI < 30:
    print("Sovrappeso")

if BMI >= 30:
    print("Obesità")
