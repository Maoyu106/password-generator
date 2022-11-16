
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
#solution one
password = ""

for l in range(1, nr_letters +1):
  final_letters = random.choice(letters)
  password += final_letters
for s in range(1, nr_symbols +1):
  final_symbols = random.choice(symbols)
  password += final_symbols
for n in range(1, nr_numbers + 1):
  final_numbers = random.choice(numbers)
  password += final_numbers

print(password)

#solution two
password_list = []

for l in range(1, nr_letters +1):
  final_letters = random.choice(letters)
  password_list += final_letters
for s in range(1, nr_symbols +1):
  final_symbols = random.choice(symbols)
  password_list.append(final_symbols)
for n in range(1, nr_numbers + 1):
  final_numbers = random.choice(numbers)
  password_list.append(final_numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char
  
print(f"Your password is {password}")