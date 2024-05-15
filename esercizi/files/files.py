import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.path.isfile(os.getcwd()+"//files.py"))

file = open("test-file.txt")
print(file.read())

file.close()

file = open("C:\\Users\\mattia.folcarelli\\Desktop\\nuovo-file.txt","w")
file.write("testo")

file.close()