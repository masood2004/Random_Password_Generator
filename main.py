import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
ask_shuffle = input("Do you want to shuffle in your password? (YES OR NO) ")

password = ""
password_list = []

if ask_shuffle == "YES" or ask_shuffle == "yes":
    for char in range(1, nr_letters + 1):
        random_char = random.choice(letters)
        password_list += random_char

    for char in range(1, nr_symbols + 1):
        random_symbol = random.choice(symbols)
        password_list += random_symbol

    for char in range(1, nr_numbers + 1):
        random_number = random.choice(numbers)
        password_list += random_number

    random.shuffle(password_list)

    for char in password_list:
        password += char

    print(password)

elif ask_shuffle == "NO" or ask_shuffle == "no":

    for char in range(1, nr_letters + 1):
        random_char = random.choice(letters)
        password += random_char

    for char in range(1, nr_symbols + 1):
        random_symbol = random.choice(symbols)
        password += random_symbol

    for char in range(1, nr_numbers + 1):
        random_number = random.choice(numbers)
        password += random_number

    print(password)

else:
    print("Something went wrong! Please try again.")