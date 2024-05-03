# write a program that asks a user to guess which Instagram account has more followers and awards marks out of 50
import random

import data_base
score = 0


def options(accounts):
    name = accounts['Name']
    description = accounts['Profession']
    country = accounts['Country']
    return f'{name}, {description} from {country}'


def choices(acc1, acc2, c):
    if acc1 > acc2 and c == 1:
        return True
    elif acc1 > acc2 and c == 2:
        return False
    elif acc1 < acc2 and c == 1:
        return False
    else:
        return True


account2 = random.choice(data_base.instagram_accounts)
continue_game = True
while continue_game:
    account1 = account2
    account2 = random.choice(data_base.instagram_accounts)
    while account1 == account2:
        account2 = random.choice(data_base.instagram_accounts)
    print('Which one of the following has a higher following on Instagram?')
    print()
    print(f'Option 1: {options(account1)}')
    print('Or')
    print(f'Option 2 : {options(account2)}')
    choice = int(input('Enter 1 or 2 : '))
    f_account1 = account1['Followers']
    f_account2 = account2['Followers']

    is_correct = choices(f_account1, f_account2, choice)

    if is_correct:
        score += 1
        print(f'Correct! Your score is {score}')
        if score == 20:
            print('You won!')
            continue_game = False
    else:
        print(f'Game over! Your score is {score}')
        continue_game = False
