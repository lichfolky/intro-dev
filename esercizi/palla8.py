# coding=utf-8
import random

risposte = [
    "Per quanto posso vedere, sì",
    "È certo",
    "È decisamente così",
    "Molto probabilmente",
    "Le prospettive sono buone",
    "I segni indicano di sì",
    "Senza alcun dubbio",
    "Sì",
    "Sì, senza dubbio",
    "Ci puoi contare",
    "È difficile rispondere, prova di nuovo",
    "Rifai la domanda più tardi",
    "Meglio non risponderti adesso",
    "Non posso predirlo ora",
    "Concentrati e rifai la domanda",
    "Non ci contare",
    "La mia risposta è no",
    "Le mie fonti dicono di no",
    "Le prospettive non sono buone",
    "Molto incerto",
]

# print(random.randint(1,6))

numero = random.randint(0, len(risposte) - 1)
# print(risposte[numero])

print(random.choice(risposte))
