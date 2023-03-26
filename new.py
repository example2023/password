import random

s = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

len_pas = int(input("Укажите длину пароля  "))

password = ''

for x in range(len_pas):
    password += random.choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')

print(password)
