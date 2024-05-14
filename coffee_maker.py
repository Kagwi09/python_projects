# write a program that would be used in a coffee making machine
# this machine should also be capable of receiving money and dispensing change
# the command 'off' should turn it off and 'report' should give a balance of all ingredients and change in the machine

import data_base

latte = data_base.menu[2]['latte']
espresso = data_base.menu[1]['espresso']
cappuccino = data_base.menu[3]['cappuccino']
macchiato = data_base.menu[4]['macchiato']
coffee_capacity = data_base.coffee_maker_capacity
sugar_cost = data_base.menu[0]['sugar_cost']


def water_balance(item):
    h2_balance = coffee_capacity[0]['ingredients']['water'] - item['ingredients']['water']
    return f"{h2_balance}"


w1 = int(water_balance(latte))
w2 = int(water_balance(espresso))
w3 = int(water_balance(cappuccino))
w4 = int(water_balance(macchiato))


def coffee_balance(item):
    c_balance = coffee_capacity[0]['ingredients']['coffee'] - item['ingredients']['coffee']
    return f'{c_balance}'


c1 = int(coffee_balance(latte))
c2 = int(coffee_balance(espresso))
c3 = int(coffee_balance(cappuccino))
c4 = int(coffee_balance(macchiato))


def milk_balance(item):
    m_balance = coffee_capacity[0]['ingredients']['milk'] - item['ingredients']['milk']
    return f'{m_balance}'


m1 = int(milk_balance(latte))
m2 = int(milk_balance(espresso))
m3 = int(milk_balance(cappuccino))
m4 = int(milk_balance(macchiato))


def proceed(item, cost1):
    print('Please insert money')
    sh_5 = int(input('How many sh. 5 coins ? : '))
    sh_10 = int(input('How many sh. 10 coins ? : '))
    sh_20 = int(input('How many sh. 20 coins ? : '))
    sh_40 = int(input('How many sh. 40 coins ? : '))
    sh_50 = int(input('How many sh. 50 notes ? : '))
    sh_100 = int(input('How many sh. 100 notes ? : '))
    sh_200 = int(input('How many sh. 200 notes ? : '))
    sh_500 = int(input('How many sh. 500 notes ? : '))
    sh_1000 = int(input('How many sh. 1000 notes ? : '))
    total_input = (sh_5 * 5) + (sh_10 * 10) + (sh_20 * 20) + (sh_40 * 40) + \
                  (sh_50 * 50) + (sh_100 * 100) + (sh_200 * 200) + (sh_500 * 500) + (sh_1000 * 1000)

    if total_input >= cost:
        change = total_input - cost
        print(f'Your total input is sh.{total_input}')
        print(f'Your balance is sh.{change}')
        coffee_capacity[1]['change'] += cost

        # Update quantities of ingredients
        coffee_capacity[0]['ingredients']['water'] -= item['ingredients']['water']
        coffee_capacity[0]['ingredients']['coffee'] -= item['ingredients']['coffee']
        coffee_capacity[0]['ingredients']['milk'] -= item['ingredients']['milk']
    else:
        print('Insufficient funds')
        proceed(item, cost1)


cost = 0
another_order = True
while another_order:
    choice = input('Select your beverage(latte, espresso, cappuccino, macchiato) : ')
    if choice.lower() == 'latte':
        if w1 >= 0 and c1 >= 0 and m1 >= 0:
            sugar = input('Do you want sugar? (Y/N) : ')
            if sugar.lower() == 'y':
                sachets = int(input('How many sachets ? : '))
                cost = int(latte['cost'] + (sachets * sugar_cost))
                print(f'The total cost is sh.{cost}')
            elif sugar.lower() == 'n':
                cost = int(latte['cost'])
                print(f'The total cost is {cost}')
            else:
                print('Invalid input')
                continue

            proceed(latte, cost)
            w1 = int(water_balance(latte))
            c1 = int(coffee_balance(latte))
            m1 = int(milk_balance(latte))
        else:
            if w1 == 0 or c1 == 0 or m1 == 0:
                print('Insufficient ingredients, please select another item')
                continue
    elif choice.lower() == 'espresso':
        if w2 >= 0 and c2 >= 0 and m2 >= 0:
            sugar = input('Do you want sugar? (Y/N) : ')
            if sugar.lower() == 'y':
                sachets = int(input('How many sachets ? : '))
                cost = int(espresso['cost'] + (sachets * sugar_cost))
                print(f'The total cost is {cost}')
            elif sugar.lower() == 'n':
                cost = int(espresso['cost'])
                print(f'The total cost is {cost}')
            else:
                print('Invalid input')
                continue
            proceed(espresso, cost)
            w2 = int(water_balance(espresso))
            c2 = int(coffee_balance(espresso))
            m2 = int(milk_balance(espresso))
        else:
            if w2 == 0 or c2 == 0 or m2 == 0:
                print('Insufficient ingredients, please select another item')
                continue
    elif choice.lower() == 'cappuccino':
        if w3 >= 0 and c3 >= 0 and m3 >= 0:
            sugar = input('Do you want sugar? (Y/N) : ')
            if sugar.lower() == 'y':
                sachets = int(input('How many sachets ? : '))
                cost = int(cappuccino['cost'] + (sachets * sugar_cost))
                print(f'The total cost is {cost}')
            elif sugar.lower() == 'n':
                cost = int(cappuccino['cost'])
                print(f'The total cost is sh.{cost}')
            else:
                print('Invalid input')
                continue
            proceed(cappuccino, cost)
            w3 = int(water_balance(cappuccino))
            c3 = int(coffee_balance(cappuccino))
            m3 = int(milk_balance(cappuccino))
        else:
            if w3 == 0 or c3 == 0 or m3 == 0:
                print('Insufficient ingredients, please select another item')
                continue
    elif choice.lower() == 'macchiato':
        if w4 >= 0 and c4 >= 0 and m4 >= 0:
            sugar = input('Do you want sugar? (Y/N) : ')
            if sugar.lower() == 'y':
                sachets = int(input('How many sachets ? : '))
                cost = int(macchiato['cost'] + (sachets * sugar_cost))
                print(f'The total cost is {cost}')
            elif sugar.lower() == 'n':
                cost = int(macchiato['cost'])
                print(f'The total cost is {cost}')
            else:
                print('Invalid input')
                continue
            proceed(macchiato, cost)
            w4 = int(water_balance(macchiato))
            c4 = int(coffee_balance(macchiato))
            m4 = int(milk_balance(macchiato))
        else:
            if w4 == 0 or c4 == 0 or m4 == 0:
                print('Insufficient ingredients, please select another item')
                continue
    elif choice.lower() == 'off':
        print('Goodbye')
        another_order = False
    elif choice.lower() == 'report':
        print(f"Water :{coffee_capacity[0]['ingredients']['water']} ml\nCoffee : "
              f"{coffee_capacity[0]['ingredients']['coffee']} g\n Milk : {coffee_capacity[0]['ingredients']['milk']}"
              f" ml\nBalance : sh.{coffee_capacity[1]['change']}")
    else:
        print('Invalid input')
        continue
