# write  program that generates a strong password
# the password can be as long as your like
# it must contain letters, numbers and symbols
# the program will be done in easy level
# this means that the characters in the password will be ordered
import random

print('Welcome to the password generator, This is the easy level.')
input1 = int(input('How many letters do you want in your password? : '))
input2 = int(input('How many numbers do you want in your password? : '))
input3 = int(input('How many symbols do you want in your password? : '))
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', ';', ':', '<', '>', '/', '?']
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'q',
              'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha = random.choices(alpha_list, k=input1)
num = random.choices(num_list, k=input2)
sym = random.choices(sym_list, k=input3)
print('Your password is :', end=' ')
for a in alpha:
    print(a, end='')
for b in num:
    print(b, end='')
for c in sym:
    print(c, end='')
