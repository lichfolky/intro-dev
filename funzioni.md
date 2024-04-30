
import random

print(random.randint(3, 9))

random numero

        print('hello %s' % x)




# todo
pip
venv, virtualenv
https://docs.python.org/3/library/venv.html

python -m venv /path/to/new/virtual/environment

On Windows, invoke the venv command as follows:

c:\>Python35\python -m venv c:\path\to\myenv
Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:

c:\>python -m venv c:\path\to\myenv

python -m pip install SomePackage

https://docs.python.org/


sum(range(4))

break


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
