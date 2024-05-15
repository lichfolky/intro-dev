
file = open("test-file.txt", "r")
# print(file.read()) TODO MATTIA

# print("codifica:", ord('Z'))

# ord() -> chr() 

## i caratteri tra 98 e 122 sono le lettere da a a z
## i caratteri tra 65 e 90 sono le lettere da A a Z

## print(file.readline(), end="")


# conta = 0
# for x in file:
#   print(conta,") ", x, sep="", end="")
#   conta = conta + 1
# file.close()

# vocali = 0
# num_parole = 0
# for line in file:
#     parole = line.split()
#     num_parole += len(parole)

#     for char in line:
#         if char in ["a", "e", "i", "o", "u"]:
#             vocali += 1

# print("il file contiene", vocali, "vocali e", num_parole, "parole")
# file.close()


# copia un file in un altra destinazione
def copia_file(src, des):
     file = open(src, "r")
     copia_file = open(des, "w")
     for line in file:
          copia_file.write(line)
     copia_file.close()
     file.close()

def codifica_file(src, des):
     file = open(src, "r")
     copia_file = open(des, "w")
     for line in file:
          linea_criptata = cripta(line, 1)
          copia_file.write(linea_criptata)
     copia_file.close()
     file.close()

def cripta(testo, offset):
     testo_criptato = ""
     for char in testo:
          cod_char = ord(char) + offset
          testo_criptato += chr(cod_char)
     return testo_criptato

def decripta(file, offset):
     file = open(file, "r")
     for line in file:
          testo_decriptato = ""
          for char in line:
               cod_char = ord(char) - offset
               testo_decriptato += chr(cod_char)
          print(testo_decriptato)
     file.close()

#copia_file("test-file.txt", "C:\\Users\\mattia.folcarelli\\Desktop\\copia.txt")
codifica_file("test-file.txt", "C:\\Users\\mattia.folcarelli\\Desktop\\fileCodificato.txt")
## print(os.path.exists("esercizi/test-file.txt"))
decripta("C:\\Users\\mattia.folcarelli\\Desktop\\fileCodificato.txt", 1)