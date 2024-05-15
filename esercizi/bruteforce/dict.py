## https://github.com/danielmiessler/SecLists/tree/master/Passwords

fileStream = open("passwords-1000.txt")
for line in fileStream:
    print(line)
fileStream.close()