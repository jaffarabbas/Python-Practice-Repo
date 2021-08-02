import random
import string


class Random:

    def get_random_string(self, length_char, length_num):
        letters = string.ascii_letters
        number = string.digits
        result_str = ''.join(random.choice(letters) for i in range(length_char)) + ''.join(
            random.choice(number) for i in range(length_num))
        password = ''.join(random.choice(result_str) for i in range(length_char + length_num))
        print(password)


obj = Random()

number = int(input("enter length of number : "))
letter = int(input("enter length of letter : "))

print(obj.get_random_string(letter, number))



