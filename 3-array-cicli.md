## array / liste

```python

animals = ['spider', 'frog', 'snail', 'bat', 'slug', 'bear']

animals[1]` # contiene 'frog'

numeri = [3, 2, 5, 6]
animali = ["leone", "panda", "gatto", "merlo", "tigre"]

matrice = [[1,2,3],
           [4,5,6],
           [7,8,9]]

bicchieri = [True, False, False]
``` 

## range
```
list(range(0, 5))

```
## Flow charts e Pseudocodice

...

## Cicli

```python
while true:
    if(finito):
        break
```
variabile canarino

## Cicli for

```python
for x in range(0, 5):
    print(x)
```
```python
for i in range(0, len(animals)):
    print(i, animals[i])
```

```python
for animal in animals:
    print(animal)
```

## for per contare

```python
array = [3, 2, 5, 6]
cont = 0
for i in array:
    if condizione:
        cont++
```

## for per accumulare

```python
array = [3, 2, 5, 6]
acc = 0
for i in array:
    if condizione:
        acc += acc
```