mie_parole = ["il", "mattino", "ha","l\'oro", "in", "bocca"]

def unisci_parole(parole):
    frase = ""
    for parola in parole:
        if frase == "" :
            frase = parola
        else:
            vecchia_frase = frase
            frase = vecchia_frase + " " + parola
    return frase

print(unisci_parole(mie_parole))




# frase = "il mattino ha l\"oro in bocca"
