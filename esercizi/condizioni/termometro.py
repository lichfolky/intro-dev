temperatura = int(input("Inserisci la temperatura "))

# stampa "fa freddo" se la temperatura è bassa, 
# "fa caldo" se è alta

if temperatura < 23:
    print("fa freddo")
else:
    print("fa caldo")

print("anzi")

if temperatura < 18:
    print("fa freddissimo")
else:
    if(temperatura < 23):
        print("fa freddo")
    else:
        if(temperatura<26):
             print("è ok")
        else:
            if(temperatura < 30):
                print("fa caldo")
            else:
                if(temperatura < 40):
                    print("fa caldissimo")
                else:
                    print("💀")

    


# -9999999 fa freddissimo 18 fa freddo 23 è ok 26 fa caldino 30 fa caldo 40 fa caldissimo 99999