# Dato l'array ["Hello", "World","in" ,"a","frame"] creare:

# *********
# * Hello *
# * World *
# * in    *
# * a     *
# * frame *
# *********

mie_parole = ["Hellooo", "World", "in", "a", "frame"]

def numero_massimo_di_lettere(parole):
    max_char = 0
    for parola in parole:
        if len(parola) > max_char:
            max_char = len(parola)
    return max_char


def printCornicetta(parole):
    max_char = numero_massimo_di_lettere(parole)
    print("*" * (max_char + 4))
    for parola in parole:
        print("* " + parola, end="")
        for i in range (max_char - len(parola)):
            print(" ", end="")
        print(" *")
    print("*" * (max_char + 4))

printCornicetta(mie_parole)

# Data una parola creare tutti gli anagrammi possibili (permutazioni)
# es:
# cane
# ance
# cena

# Data una parola valutare se è palindroma

# anna
# i topi non avevano nipoti
