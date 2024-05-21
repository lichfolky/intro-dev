password_generate = []
password = "" 

# Non mettere più di 5 nel range
# per terminare premere control + c nel terminale
for y in range(4):
    if y == 0:
        for x in range(98,123):
            password = chr(x)
            password_generate.append(password)
    else:
        new_password_generate = []
        for y in password_generate:
            for x in range(98,123):
                password = y + chr(x)
                new_password_generate.append(password)
        password_generate = new_password_generate

print(password_generate)