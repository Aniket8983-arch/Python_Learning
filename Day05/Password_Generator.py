import random



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
'''for i in range(nr_letters):
    i = random.choice(letters)
    print(i , end = "")
for i in range(nr_symbols):
    i= random.choice(symbols)
    print(i , end = "")
for i in range(nr_numbers):
    i= random.choice(numbers)
    print(i , end = "")'''
list_new = []
for i in range(nr_letters):
    list_new.append(random.choice(letters))
for i in range(nr_symbols):
    list_new.append(random.choice(symbols))
for i in range(nr_numbers):
    list_new.append(random.choice(numbers))
print(list_new)
random.shuffle(list_new)
print(list_new)
for i in list_new:
    print(i, end ="")