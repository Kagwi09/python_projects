# write a program that does basic math calculations(add, subtract, multiply, divide) from user input
def calculator(num1, num2, sym):
    if sym == '+':
        return num1 + num2
    elif sym == '-':
        return num1 - num2
    elif sym == '*':
        return num1 * num2
    elif sym == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation!"


def choices():
    number1 = float(input('Enter the first number: '))
    continue_operation = True
    while continue_operation:
        symbol = input('Enter the operation (+, -, *, /): ')
        number2 = float(input('Enter the second number: '))

        result = calculator(number1, number2, symbol)

        choice = input('Do you want to continue? Input(y) to continue operation, (n) to start'
                       ' a new operation and (x) to exit? ')
        if choice.lower() == 'n':
            print(f'The result is {round(result, 3)}')
            choices()
        elif choice.lower() == 'y':
            number1 = result
            print(f'The result is {round(result, 3)}')
        elif choice.lower() == 'x':
            print(f'The result is {round(result, 3)}')
            continue_operation = False
        else:
            print(f'The result is {round(result, 3)}')
            print(f'Invalid input')
            choices()
            continue


choices()
