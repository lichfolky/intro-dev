## Conta le vocali e il numero di lettere di una stringa
def conta_lettere(stringa):
    stringa_lower = stringa.lower()
    stringa_lower = stringa_lower.strip() # trim della stringa
    stringa_lower = stringa_lower.replace(" ", "")

    print(stringa_lower)
    vocali = ['a','e','i','o','u']
    # print(stringa[0])
    conta_lettere = 0
    conta_vocali = 0

    for lettera in stringa_lower:
        if lettera in vocali:
            conta_vocali += 1
        conta_lettere = conta_lettere + 1

    print("lettere: ", conta_lettere, " vocali: ", conta_vocali, ''.join(vocali) )

    print("parola lowercase".upper())
    print("PAROLA IN UPPERCASE".lower())
    return [conta_lettere,conta_vocali]


risultato = conta_lettere("CIAO           ciao Come va?   ")
print("lettere: ", risultato[0], " vocali: ", risultato[1])
