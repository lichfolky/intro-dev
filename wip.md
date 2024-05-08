print('hello %s' % x)

## pip

`python -m pip install SomePackage`

## venv, virtualenv
https://docs.python.org/3/library/venv.html

python -m venv /path/to/new/virtual/environment

On Windows, invoke the venv command as follows:

`c:\>Python35\python -m venv c:\path\to\myenv`
Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:

`c:\>python -m venv c:\path\to\myenv`

## db

https://www.freecodecamp.org/news/how-to-read-and-write-data-to-a-sql-database-using-python/

Telegram bot


https://www.w3schools.com/python/python_operators.asp

https://code.visualstudio.com/docs/python/linting
 
magic comments # coding=utf-8

obj

init

main

decoratori

import sys
             while True:
                 print('Type exit to exit.')
                 response = input()
                 if response == 'exit':
                     sys.exit()
                 print('You typed ' + response + '.')