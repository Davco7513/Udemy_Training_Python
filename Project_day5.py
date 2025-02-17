import string
import random

l = string.ascii_letters
d = string.digits
p = string.punctuation
print("Welcome to the PyPassword Generator !")
letters = int(input("How many letters would you like in your password ?\n"))
digits = int(input("How many digits would you like in your password ?\n"))
symbols = int(input("How many symbols would you like in your password ?\n"))
password = ''.join(random.sample(l,letters))
password += ''.join(random.sample(d,digits))
password += ''.join(random.sample(p,symbols))
password_list = list(password)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ''.join(password_list)
print(password)

