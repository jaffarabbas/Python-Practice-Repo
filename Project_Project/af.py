import random
import string

if __name__ == '__main__':
    print("\nWelcome to the password generator site!")

    passw = input('\nEnter the password: ')

    # length = int(input('\nEnter the length of password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbol = string.punctuation

    all = lower + upper + number + symbol

    password = ''.join(random.choice(all) for i in range(len(all)))

    print(password)
    l = list(password)
    random.shuffle(l)