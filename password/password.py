import os

file_size = os.path.getsize('password.txt')

if file_size == 0:

    while True:

        create_password = input('Create new password: ')

        confirm_password = input('Confirm password: ')

        if create_password == confirm_password:

            open_file = open('password.txt', 'w')

            saved_password = open_file.write(confirm_password)

            break

        elif create_password != confirm_password:

            print('Error, passwords do not match. Try again')

            print()

elif file_size > 0:

    i = 0

    while i < 3:

        enter_password = input('Enter password: ')

        opened_password_file = open('password.txt', 'r')

        if enter_password in opened_password_file:

            print('Subscribe to the proton guys channel')

        elif enter_password not in opened_password_file:

            i = i + 1

            print('Error, you typed in a wrong password') 

            print()

            print(f'Tries left: {3-i}')

    if i == 3:

        print('Closing program. Suspicious activity detcted')

        exit()
