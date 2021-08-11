import random
import string

if __name__ == '__main__':
    print(' Welcome to Password generator!')

    length = int(input('\nEnter the length of password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all, length)

    password = "".join(temp)

    print(password)
