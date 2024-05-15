# match

carta forbici sasso

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


Utilizzi avanzati:
https://peps.python.org/pep-0636/#matching-sequences

https://machinelearningtutorials.org/python-match-statements-tutorial-with-examples/

# Esercizio
list(range(0, 5))

gioco impiccato
