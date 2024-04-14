# write a program that encrypts or decrypts input from the user
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']


def caesar_encrypt(message, shift):
    encrypted_message = ' '

    for i in message:
        if i in alpha_list:
            index1 = alpha_list.index(i)
            index2 = (index1 + shift) % 26
            encrypted_message += alpha_list[index2]
        else:
            encrypted_message += i
    print(f'Your encrypted message is {encrypted_message}')

    # the for loop iterates through every character in the message
    # the if statement checks if the character is in the alpha_list
    # if its there, index1 checks the position of the position of item i in its list
    # index2 becomes the shift value


def caesar_decrypt(encrypted_message, shift):
    message = ' '

    for i in encrypted_message:
        if i in alpha_list:
            index1 = alpha_list.index(i)
            index2 = (index1 - shift) % 26
            message += alpha_list[index2]
        else:
            message += i
    print(f'Your decrypted message is {message}')


end = False
while not end:
    order1 = input("Input 'e' to encrypt message or 'd' to decrypt message.\n ")
    order2 = input('Enter message : .\n')
    order3 = int(input('Enter shift number. \n'))

    if order1.lower() == 'e':
        caesar_encrypt(message=order2, shift=order3)
    elif order1.lower() == 'd':
        caesar_decrypt(order2, order3)
    else:
        print("Incorrect input.")
        continue

    order4 = input("Do you want to encrypt another message? 'Y' for yes, 'N' for no.\n ")
    if order4.lower() == 'n':
        end = True
        print('Goodbye')
    elif order4.lower() == 'y':
        continue
    else:
        print('Invalid input')
        continue




