## Controlla se hai abbastanza soldi, sottraendo le spese al budget
## prendi ispirazione da funzioni-somma.py

my_budget = 300
my_spese = [299, 6, 2, 4, 7, 8, 2]


def check_budget(budget, spese):
    acc_budget = budget
    for spesa in spese:
        acc_budget = acc_budget - spesa
        ## budget = budget + spese[i]
    if acc_budget >= 0:
        return True
    else:
        return False


def check_budget2(budget, spese):
    acc_budget = budget
    for spesa in spese:
        acc_budget = acc_budget - spesa
        if acc_budget < 0:
            print("non posso permettermi: ", spesa)
            return False
        ## budget = budget + spese[i]
    if acc_budget >= 0:
        return True
    else:
        return False


if check_budget2(my_budget, my_spese):
    print("vado a fare la spesa")
