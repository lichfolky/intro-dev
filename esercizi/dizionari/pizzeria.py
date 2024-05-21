pizze = {
    "margherita": ["pomodoro", "mozzarella"],
    "diavola": ["pomodoro", "mozzarella", "salamino"],
    "quattro formaggi": ["pomodoro", "mozzarella", "gorgonzola", "fontina", "provola"],
    "farinata": ["farina di ceci", "olio"],
}

inventario = {
    "pomodoro": 10,
    "mozzarella": 10,
    "gorgonzola": 2,
    "fontina": 2,
    "provola": 3,
}

print(pizze["quattro formaggi"])


def fai_pizza(nome_pizza):
    ingredienti = pizze[nome_pizza]
    for ingr in ingredienti:
        if inventario[ingr] == 0:
            print("ingredienti finiti!!!")
            return
        inventario[ingr] -= 1


fai_pizza("quattro formaggi")
fai_pizza("quattro formaggi")
fai_pizza("quattro formaggi")

pizze["bianca"] = ["mozzarella"]

print(pizze.keys())
for pizza in pizze:
    print(pizza)
