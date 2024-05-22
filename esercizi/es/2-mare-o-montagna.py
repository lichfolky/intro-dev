punti_mare = 0
punti_montagna = 0
risposta = input("Ti piace nuotare (si o no)?")

risposta = risposta.strip()
if risposta == "si":
    punti_mare = punti_mare + 1
else:
    if risposta == "no":
        punti_montagna = punti_montagna + 1
    else:
        print("comando errato!!!")

risposta = input("Ti piace la neve (si o no)?")

risposta = risposta.strip()
if risposta == "no":
    punti_mare = punti_mare + 1
else:
    if risposta == "si":
        punti_montagna = punti_montagna + 1
    else:
        print("comando errato!!!")

risposta = input("Ti piace il freddo o il caldo?")

risposta = risposta.strip()
if risposta == "caldo":
    punti_mare = punti_mare + 1
else:
    if risposta == "freddo":
        punti_montagna = punti_montagna + 1
    else:
        print("comando errato!!!")


if punti_mare > punti_montagna:
    print("Sei da mare!")
else:
    if punti_mare < punti_montagna:
        print("Sei da montagna!")
    else:
        print("Ti va bene tutto??")