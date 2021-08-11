import string

class Test:
    tempPassword = ''
    
    def UserValue(self):
        value = input("Enter value: ")
        return value

    def userInputSuffleValue(self):
        return self.tempPassword[::-1]

    def userInputSuffleIntoNumber(self):
        temp = ''
        for i in self.tempPassword:
            temp += str(string.ascii_lowercase.index(i))
        return temp

    def FinalPassword(self):
        self.tempPassword = self.UserValue()
        return "".join(self.userInputSuffleValue() + "" + self.tempPassword + "" + self.userInputSuffleIntoNumber())


def main():
    password = Test()
    print(password.FinalPassword())


if __name__ == '__main__':
    main()
