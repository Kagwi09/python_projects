import random

import data_base

stage0 = data_base.stage0
stage1 = data_base.stage1
stage2 = data_base.stage2
stage3 = data_base.stage3
stage4 = data_base.stage4
stage5 = data_base.stage5
stage6 = data_base.stage6
print('Welcome to the hangman game!')
print(stage6)
list1 = ['clove', 'sage', 'thyme', 'mint', 'basil']
random_herb = random.choice(list1)
list2 = list(random_herb)
# print(list2)
display = []
for letter in list2:
    display += '_'
game_over = False
lives = 6
while not game_over:
    user_input = input("Enter your letter : ").lower()
    print(display)
    for position in range(len(list2)):
        letter = list2[position]
        if letter == user_input:
            display[position] = user_input
    print('Your guess is correct!')
    print(display)
    if user_input not in list2:
        lives -= 1
        if lives == 0:
            game_over = True
            print(stage0)
            print('Game over')
        if lives == 1:
            print(stage1)
            print('You have one more life')
        if lives == 2:
            print(stage2)
            print('You have two more lives')
        if lives == 3:
            print(stage3)
            print('You have 3 more lives')
        if lives == 4:
            print(stage4)
            print('You have four more lives')
        if lives == 5:
            print(stage5)
            print('You have five more lives')
    if '_' not in display:
        game_over = True
        print('You guessed correctly!')
