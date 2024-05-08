## Conta quante volte è presente il 6 in un array
numeri1 = [2, 3, 6, 6, 3, 5, 6]


def conta_numero(array, numero):
    conta = 0  # contatore
    for i in range(0, len(numeri1)):
        if array[i] == numero:
            conta += 1
    return conta


def conta_4_experts(array):
    conta = 0  # contatore
    for numero in array:
        # se il numero corrente è 6
        if numero == 6:
            conta += 1  # somma alla variabile uno, abbreviazione di conta = conta + 1
            print(numero)
    return conta


print("numero di 6 in array: ")
print(conta_numero(numeri1, 2))

numeri2 = [33, 5, 3, 6, 43, 6, 787, 44]


## Conta i numeri pari di un array
def conta_numeri_pari(array):
    numeri_pari = 0
    for numero in array:
        if numero % 2 == 0:
            numeri_pari += 1
    return numeri_pari


print("questo array: " + str(numeri2))

print("ha " + str(conta_numeri_pari(numeri2)) + " numeri pari")

## Controlla se hai abbastanza soldi, sottraendo le spese al budget
## prendi ispirazione da funzioni-somma.py
my_budget = 100
spese = [1, 6, 2, 4, 7, 8, 2]

def check_budget(my_budget, spese):