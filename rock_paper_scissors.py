# write a program that plays rock, paper, scissors with a user
# the user will be required to input a prompt that will be compared to the randomly generated computer prompt
import random

user_prompt = input('Rock, paper, Scissors ? : ')
list1 = ['Rock', 'Paper', 'Scissors']
computer_prompt = random.choice(list1)
print(computer_prompt)
str1 = "It's a draw !"
str2 = 'Rock wins !'
str3 = 'Paper wins !'
str4 = 'Scissors wins !'
if user_prompt == 'Rock' or user_prompt == 'rock':
    if computer_prompt == 'Rock':
        print(f'{str1}')
    elif computer_prompt == 'Paper':
        print(f'{str3}')
    else:
        print(f'{str2}')
if user_prompt == 'Paper' or user_prompt == 'paper':
    if computer_prompt == 'Paper':
        print(f'{str1}')
    elif computer_prompt == 'Rock':
         print(f'{str3}')
    else:
        print(f'{str4}')
if user_prompt == 'Scissors' or user_prompt == 'scissors':
    if  computer_prompt == 'Scissors':
        print(f'{str1}')
    elif computer_prompt == 'Rock':
         print(f'{str2}')
    else:
        print(f'{str4}')

