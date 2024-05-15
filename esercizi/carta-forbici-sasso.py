scelta_giocatore = input("Scegli carta, forbici o sasso: ")
print(scelta_giocatore)

# se la scelta_giocatore è "sasso"
# if scelta_giocatore == "sasso":
#     print("CARTA!")
# elif scelta_giocatore == "forbici":
#     print("SASSO!")
# else:
#     print("FORBICI!")

match scelta_giocatore:
    case "sasso" | "Sasso" | "SASSO":
        print("CARTA!")
    case "forbici":
        print("SASSO!")    
    case "carta":
        print("FORBICI!")
    case _:
        print("inserisci un simbolo valido")