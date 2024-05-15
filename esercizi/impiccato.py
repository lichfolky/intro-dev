parola_segreta = "sole"
print("_ " * len(parola_segreta))
lettera = input("Inserisci lettera: ")
if lettera in parola_segreta:
    print("trovato")
