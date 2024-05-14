## print(file.read())
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
def copia_file(srg, des):
     file = open(srg, "r")
     copia_file = open(des, "w")
     for line in file:
          copia_file.write(line)
     copia_file.close()
     file.close()

copia_file("test-file.txt", "C:\\Users\\mattia.folcarelli\\Desktop\\copia.txt")
## print(os.path.exists("esercizi/test-file.txt"))