import random

gioco_finito = False
punti = 0
while not gioco_finito:
    scelte = ["carta", "forbici", "sasso"]
    scelta_pc = random.choice(scelte)

    finito = False
    while not finito:
        scelta_giocatore = input("Scegli carta, forbici o sasso: ")
        # match scelta_giocatore:
        #    case "sasso"|"forbici"|"carta":
        #        finito = True
        if scelta_giocatore in ["sasso", "forbici", "carta"]:
            finito = True

    print("Il COMPUTER HA SCELTO", scelta_pc)

    # se la scelta_giocatore è "sasso"
    # if scelta_giocatore == "sasso":
    #     print("CARTA!")
    # elif scelta_giocatore == "forbici":
    #     print("SASSO!")
    # else:
    #     print("FORBICI!")

    match [scelta_giocatore, scelta_pc]:
        case ["sasso", "forbici"] | ["carta", "sasso"] | ["forbici", "carta"]:
            print("HAI VINTO")
            punti += 1
        case ["sasso", "sasso"] | ["carta", "carta"] | ["forbici", "forbici"]:
            print("PAREGGIO")
        case ["forbici", "sasso"] | ["sasso", "carta"] | ["carta", "forbici"]:
            print("HAI PERSO")
            punti -= 1
        case _:
            print("failure")

    print("hai ottenuto", punti, "punti!")
    risposta = input("Vuoi rigiocare (s/n)? ")
    if risposta == "n":
        gioco_finito = True
