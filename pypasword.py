import random
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = list(alpha)
num = "0123456789"
symbol = "'?/>.<,:;{}|\][+=_-)(~`!@#$%^&*"
[num, symbol] =[list(num), list(symbol)]
print(alpha, num, symbol)
num_count = input("how many letters in password \t")
sym_count = input("how many letters in password \t")
alpha_count = input("how many letters in password \t")

num_count = int(num_count)
sym_count = int(sym_count)
alpha_count = int(alpha_count)
password = []
for char in range(1, num_count + 1):
    password.append(random.choice(num))
for char in range(1, sym_count + 1):
    password.append(random.choice(symbol))
for char in range(1, alpha_count + 1):
    password.append(random.choice(alpha))

random.shuffle(password)
password = "".join(password)

print(f'your password is {password}')
