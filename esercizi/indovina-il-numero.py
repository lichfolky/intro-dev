# coding=utf-8
numero_segreto = 9

print("-" * 40)
print(" " * 10 + "INDOVINA IL NUMERO")
print("-" * 40)

print("Il numero segreto e' un numero tra 0 e 90,")
print("cerca di indovinarlo in meno tentativi")
print("possibili approfittando dei suggerimenti")
print("i suggerimenti sono: oceano, acqua, fuochino, fuoco")
print("per uscire premi contemporaneamente i pulsanti CTRL e C \n")

numero = int(input("inserisci un numero: "))
finito = False
while not finito:
    # controllo se il numero è stato trovato
    # se sì metto finito a True
    if numero_segreto == numero:
        finito = True
    else:
        # altrimenti dico di quanto sta sbagliando (acqua, fuoco...)
        if numero > numero_segreto:
            differenza = numero - numero_segreto
        else:
            differenza = numero_segreto - numero

        if differenza <= 5:
            print("Fuoco!!")
        else:
            if differenza <= 10:
                print("Fuochino!!")
            else:
                if differenza <= 20:
                    print("Acqua!")
                else:
                    print("OCEANO!!!")

        numero = int(input("nuovo numero: "))

print("Hai trovato il numero " + str(numero_segreto))
