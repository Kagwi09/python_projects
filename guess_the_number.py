# write a program that prompts a user to guess a number from a specified range
# the guessing game should come in two mode, easy and hard
import random


def guess_game():
    print("Welcome to 'Guess the number game'")
    mode = input("Enter 'easy' for easy mode and 'hard' for hard mode : ").lower()
    i = random.randrange(1, 51)

    def wrong_input(j):
        if not (j == 'easy' or j == 'hard'):
            print("Invalid input.")
            guess_game()

    wrong_input(mode)

    print(i)
    end_game = False
    easy_lives = 10
    hard_lives = 5
    while not end_game:
        guess = int(input('Enter a number between 1 and 50 : '))

        def too_high_too_low(a, b):
            if a > b:
                print('Wrong guess! Number is too high')
            elif a < b:
                print('Wrong guess! Number is too low')

        too_high_too_low(guess, i)

        if mode == 'easy':
            if guess == i:
                print('Correct guess!')
                end_game = True
            else:
                easy_lives -= 1
                if easy_lives == 9:
                    print('Nine lives remaining')
                elif easy_lives == 8:
                    print('Eight lives remaining')
                elif easy_lives == 7:
                    print('Seven lives remaining')
                elif easy_lives == 6:
                    print('Six lives remaining')
                elif easy_lives == 5:
                    print('Five lives remaining')
                elif easy_lives == 4:
                    print('Four lives remaining')
                elif easy_lives == 3:
                    print('Three lives remaining')
                elif easy_lives == 2:
                    print('Two lives remaining')
                elif easy_lives == 1:
                    print('One life remaining')
                else:
                    print('Game over')
                    end_game = True
        elif mode == 'hard':
            if guess == i:
                print('Correct guess!')
                end_game = True
            else:
                hard_lives -= 1
                if hard_lives == 4:
                    print('Four lives remaining')
                elif hard_lives == 3:
                    print('Three lives remaining')
                elif hard_lives == 2:
                    print('Two lives remaining')
                elif hard_lives == 1:
                    print('One lives remaining')
                else:
                    print('Game over')
                    end_game = True


guess_game()
