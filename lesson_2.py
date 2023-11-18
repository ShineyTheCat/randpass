from random import choice

symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght_pass = int(input("Введите длину вашего пароля: "))
shakal = ""

for i in range(lenght_pass):
    shakal += choice(symbol)

print("Ваш пароль:", shakal)
print("0_o")
