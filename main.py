import random

pasword = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pregunta = int (input("De cuanto caracteres deseas tu contraseña :"))
count = ""

for i in range(pregunta):
    letra= random.choice(pasword)
    count = count + letra
print("tu contraseña es:", count)
