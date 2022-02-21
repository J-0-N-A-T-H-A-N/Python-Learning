import random

chars_num = int(input("How many characters would you like? \n"))
specials_num = int(input("How many special characters would you like? \n"))
digits_num = int(input("How many numbers would you like? \n"))
letters_num = chars_num - specials_num - digits_num

letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
specials="!£$%^&*()@~|?><;:'~{}[]"

letters_list=[]
specials_list=[]
digits_list=[]

for item in letters:
    letters_list.append(item)
for item in specials:
    specials_list.append(item)
for item in range(10):
    digits_list.append(item)
password=[]
for letter in range(letters_num):
    password.append(random.choice(letters_list))
for special in range(specials_num):
    password.append(random.choice(specials_list))
for digit in range(digits_num):
    password.append(str(random.choice(digits_list)))

random.shuffle(password)

new_password=""
for char in password:
    new_password += char
print(f"Your new password is: {new_password}")




