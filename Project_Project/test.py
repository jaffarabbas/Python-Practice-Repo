import random
import string


# functions
# 1-taking user info
# 2-generate random pass
# 3-shuffle input in it

class User:
    name = ''


class GeneratePassword:
    password = ''
    userInputManipulatedString = ''

    def Generate(self):
        SpecialCharacters = ['!', '@', '#', '&', '%', '^', '*', '$', '_', '~']
        user = input('enter user value: ')
        passValue = random.sample(user, len(user))
        for i in passValue:
            self.userInputManipulatedString += i
        randomString = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
        randomLowerString = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        randomUpperString = ''.join(random.choice(string.digits) for i in range(4))
        randomSpecialString = ''.join(random.choice(SpecialCharacters) for i in range(4))
        tempPassword = randomLowerString + randomUpperString + randomSpecialString + randomString + self.userInputManipulatedString
        self.password = ''.join(random.choice(tempPassword) for i in range(len(tempPassword)))
        return self.password


def main():
    GeneratePasswordObject = GeneratePassword()
    print(GeneratePasswordObject.Generate())


if __name__ == '__main__':
    main()
