
```
file = open("test-file.txt")
print(file.read())

file.close()
```


coding=utf-8


```
Per modificare configurazione launcher python di vscode

    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "cwd": "${fileDirname}",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
```