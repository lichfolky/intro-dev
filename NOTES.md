23/04/2024 - [intro](intro.md)
24/04/2024 - [python, tipi di dati e variabili](python-variabili.md)
30/04/2024 - [logica e condizioni](condizioni-cicli.md)
07/05/2024 - [Array e cicli](array-cicli.md)
08/05/2024 - [Funzioni e librerie](array-cicli.md)
14/05/2024
15/05/2024
21/05/2024
22/05/2024
28/05/2024	Prova finale

## match, code, matrici

in

break

ricerca lineare

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

-1 nele liste
spam[1:4] is a list with a slice (two integers).

>>> spam = ['cat', 'bat', 'rat', 'elephant'] >>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']

+ per joinare due array

cancellare:
>>> del spam[2]

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

>>> cat = ['fat', 'black', 'loud']
 >>> size, color, disposition = cat

list.index('hello')
list.append()
list.remove(1,"ICAO")
list.sort()



----


## esercizi


impiccato

shuffle -> in quale dei tre bicchieri è?

battaglia navale

una carta casuale

## mappe files e moduli


module
docstring


Figure 5-7: A Caesar cipher 125
upper
lower

ord()<->chr()

favorite_sports = {'Ralph Williams' : 'Football',
                                 'Michael Tippett' : 'Basketball',
                                 'Edward Elgar' : 'Baseball',
                                 'Rebecca Clarke' : 'Netball',
                                 'Ethel Smyth' : 'Badminton',
                                 'Frank Bridge' : 'Rugby'}

https://realpython.com/read-write-files-python/
                                 
>>> test_file = open('c:\\Users\\<your username>\\test.txt')
>>> text = test_file.read()
>>> print(text)
There once was a boy named Marcelo
Who dreamed he ate a marshmallow
He awoke with a start
As his bed fell apart
And he found he was a much rounder fellow

>>> test_file = open('c:\\myfile.txt', 'w')
>>> test_file.write('What is green and loud? A froghorn!')
>>> test_file.close()


pickle

u>>> import pickle v>>> game_data = {
                'player-position' : 'N23 E45',
                'pockets' : ['keys', 'pocket knife', 'polished stone'],
                'backpack' : ['rope', 'hammer', 'apple'],
                'money' : 158.50
                }
w>>> save_file = open('save.dat', 'wb')
x>>> pickle.dump(game_data, save_file)
y>>> save_file.close()


>>> load_file = open('save.dat', 'rb')
>>> loaded_game_data = pickle.load(load_file)
>>> load_file.close()


## Esercizi:
- Create a Python program to copy a file.

- Messaggio in codice, iniziale 2a parola di ogni riga

## oggetti passaggio valore e referenza