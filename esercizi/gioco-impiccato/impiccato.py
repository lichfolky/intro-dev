import random

parole = []
file = open("parole.txt")
for parola in file:
    parole.append(parola.strip())
file.close()

print(parole)

parola_segreta = random.choice(parole)
gioco_finito = False
lettere_trovate = []
lettere_da_trovare = []
for lettera in parola_segreta:
    if lettera not in lettere_da_trovare:
        lettere_da_trovare += lettera
        
tentativi_falliti = 0
while not gioco_finito:
    for lettera in parola_segreta:
        if lettera in lettere_trovate:
            print(lettera, end=" ")
        else:
            print("_", end=" ")

    print(" (", tentativi_falliti, "/6)", lettere_trovate, sep="", end=" ")
    lettera = input("Inserisci lettera: ")
    if lettera in parola_segreta:
        if lettera not in lettere_trovate:
            lettere_trovate += lettera
    else:
        tentativi_falliti += 1

    if tentativi_falliti == 6:
        gioco_finito = True
        print("SEI MORTO! la parola era", parola_segreta,"!")
    
    if len(lettere_trovate) == len(lettere_da_trovare):
        gioco_finito = True
        print("HAI VINTO! la parola era", parola_segreta,"!")
