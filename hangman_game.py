import random
stage0 = ['+-------+', '|        |', '|        O', '|       /|\\', '|        /\\', '|']
stage1 = ['+-------+', '|        |', '|        O', '|       /|\\', '|        /', '|']
stage2 = ['+-------+', '|        |', '|        O', '|       /|\\', '|        ', '|']
stage3 = ['+-------+', '|        |', '|        O', '|       /|', '|        ', '|']
stage4 = ['+-------+', '|        |', '|        O', '|        |', '|        ', '|']
stage5 = ['+-------+', '|        |', '|        O', '|        ', '|        ', '|']
stage6 = ['+-------+', '|        |', '|        ', '|        ', '|        ', '|']
print('Welcome to the hangman game!')
print(f'{stage6[0]}\n{stage6[1]}\n{stage6[2]}\n{stage6[3]}\n{stage6[4]}\n{stage6[5]}')
list1 = ['clove', 'sage', 'thyme', 'mint', 'basil']
random_herb = random.choice(list1)
list2 = list(random_herb)
#print(list2)
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
            print(f'{stage0[0]}\n{stage0[1]}\n{stage0[2]}\n{stage0[3]}\n{stage0[4]}\n{stage0[5]}')
            print('Game over')
        if lives == 1:
            print(f'{stage1[0]}\n{stage1[1]}\n{stage1[2]}\n{stage1[3]}\n{stage1[4]}\n{stage1[5]}')
            print('You have one more life')
        if lives == 2:
            print(f'{stage2[0]}\n{stage2[1]}\n{stage2[2]}\n{stage2[3]}\n{stage2[4]}\n{stage2[5]}')
            print('You have two more lives')
        if lives == 3:
            print(f'{stage3[0]}\n{stage3[1]}\n{stage3[2]}\n{stage3[3]}\n{stage3[4]}\n{stage3[5]}')
            print('You have 3 more lives')
        if lives == 4:
            print(f'{stage4[0]}\n{stage4[1]}\n{stage4[2]}\n{stage4[3]}\n{stage4[4]}\n{stage4[5]}')
            print('You have four more lives')
        if lives == 5:
            print(f'{stage6[0]}\n{stage6[1]}\n{stage6[2]}\n{stage6[3]}\n{stage6[4]}\n{stage6[5]}')
            print('You have five more lives')
    if '_' not in display:
        game_over = True
        print('You guessed correctly!')





