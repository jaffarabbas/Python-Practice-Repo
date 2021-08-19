import random
import string
from tkinter import *

from copyPassword import CopyPassword


class UserInputPassword:
    password = ''
    checkValue = []
    PasswordLength = 0
    SpecialCharacters = "@$-&.%!_#"

    def main_window(self):
        # variables
        userInputWindow = Tk()
        userInputWindow.title("Random Password")
        app_width = 1000
        app_height = 600
        LengthValue = IntVar()
        LengthValue.set(15)
        self.PasswordLength = LengthValue.get()
        varValueForCheckBox = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        screen_width = userInputWindow.winfo_screenwidth()
        screen_height = userInputWindow.winfo_screenheight()
        x_cord = (screen_width / 2) - (app_width / 2)
        y_cord = (screen_height / 2) - (app_height / 2)
        copyGeneratedPassword = PhotoImage(file="images/CopyPasswordButton.png")
        generatePasswordButton = PhotoImage(file="images/EnterPasswordButton.png")
        userInputBackgroundImage = PhotoImage(file="images/userInputPasswordScreen.png")
        checkBeforeImage = PhotoImage(file="images/Checkbox.png")
        checkAfterImage = PhotoImage(file="images/checked.png")

        background_label = Label(userInputWindow, image=userInputBackgroundImage)
        CopyGeneratedPassword = copyGeneratedPassword.subsample(3, 3)
        GeneratePasswordButton = generatePasswordButton.subsample(3, 3)

        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        userInputWindow.resizable(0, 0)
        userInputWindow.geometry(f'{app_width}x{app_height}+{int(x_cord)}+{int(y_cord)}')

        Output = Text(userInputWindow, height=1, borderwidth=0,
                      width=40,
                      bg="white", font=("Corbel", 25))

        Output.place(x=122, y=219)

        InputField = Text(userInputWindow, height=1, borderwidth=0,
                          width=40,
                          bg="white", font=("Corbel", 25))

        InputField.place(x=122, y=323)

        CheckBox_1 = Checkbutton(userInputWindow, variable=varValueForCheckBox[0], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=309, y=472)
        CheckBox_2 = Checkbutton(userInputWindow, variable=varValueForCheckBox[1], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=290, y=515)
        CheckBox_3 = Checkbutton(userInputWindow, variable=varValueForCheckBox[2], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=585, y=470)
        CheckBox_4 = Checkbutton(userInputWindow, variable=varValueForCheckBox[3], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=630, y=518)
        CheckBox_5 = Checkbutton(userInputWindow, variable=varValueForCheckBox[4], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=836, y=471)

        CheckBox_6 = Checkbutton(userInputWindow, variable=varValueForCheckBox[5], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=837, y=515)

        def state():
            self.checkValue.clear()
            for i in varValueForCheckBox:
                self.checkValue.append(int(i.get()))
            return self.checkValue

        def Copy():
            CopyPassword.CopyPassword(Output.get("1.0", END))

        CopyButton = Button(userInputWindow, image=CopyGeneratedPassword, compound=LEFT, bg='white', borderwidth=0,
                            command=Copy)
        CopyButton.place(x=830, y=209)

        def checkCheckBox():
            # Generate button work
            self.password += InputField.get("1.0", END)
            print("main line : ", self.password, "\n field: ", InputField.get("1.0", END), "\n Shffle : "
                  , self.userInputShuffleValue(), "\n number", self.userInputShuffleIntoNumber(), "\n   reverse"
                  , self.userInputReverseValue())
            print('State: ', state())
            # Display text field work
            Output.configure(state="normal")
            self.password = ''
            Output.delete('1.0', END)
            Output.insert(END, self.GeneratePassword(list(state())))
            Output.configure(state='disabled')
            self.PasswordLength = LengthValue.get()

        GenerateButton = Button(userInputWindow, image=GeneratePasswordButton, compound=LEFT, bg='white',
                                borderwidth=0, command=checkCheckBox)
        GenerateButton.place(x=830, y=311)

        userInputWindow.mainloop()

    def GeneratePassword(self, CheckList):
        print("1", CheckList)
        tempPassword = ''
        try:
            if CheckList[0] == 1:
                tempPassword += self.UserInputPasswordPlacing(self.password, self.userInputShuffleValue(), "")
            if CheckList[1] == 1:
                tempPassword += self.UserInputPasswordPlacing(self.userInputShuffleValue(), self.password, "")
            if CheckList[2] == 1:
                tempPassword = self.UserInputPasswordPlacing(self.userInputShuffleValue(),
                                                             self.userInputShuffleIntoNumber(), self.password)
            if CheckList[3] == 1:
                tempPassword += self.UserInputPasswordPlacing(self.userInputReverseValue(),
                                                              self.specialCharacterShuffle(1), self.password)
            if CheckList[4] == 1:
                tempPassword += self.UserInputPasswordPlacing(self.userInputShuffleValue(),
                                                              self.specialCharacterShuffle(1), self.password)
            if CheckList[5] == 1:
                tempPassword += self.GenerateDefaultPassword()
            if CheckList.count(0) == 6:
                print("Error!")

        except EXCEPTION:
            print(EXCEPTION)

        return tempPassword

    def userInputShuffleValue(self):
        return ''.join(random.choice(self.password) for i in range(len(self.password)))

    def userInputReverseValue(self):
        return self.password[::-1]

    def userInputShuffleIntoNumber(self):
        print("hii : ", self.password)
        value = 'jaffar'
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        letterListOfNumber = ''
        for i in str(self.password):
            indexes = [x for x in range(len(letters)) if letters[x] == i]
            print(indexes)
            letterListOfNumber += str(indexes.pop())

        print(letterListOfNumber)
        return letterListOfNumber

    # shuffle the special characters
    def specialCharacterShuffle(self, rangeValue):
        return "".join(random.sample(self.SpecialCharacters, rangeValue))

    # generate random password by default
    def GenerateDefaultPassword(self):
        return "".join(self.specialCharacterShuffle(1) + "" + self.userInputShuffleValue() + ""
                       + self.password + "" + self.specialCharacterShuffle(1) + self.userInputShuffleIntoNumber() + ""
                       + self.specialCharacterShuffle(1))

    # return password string
    def UserInputPasswordPlacing(self, firstValue, secondValue, thirdValue):
        return firstValue + "" + secondValue + "" + thirdValue

    # # distribute password length
    # def LengthDistribution(self, length, numberOfBreaks, index):
    #     distributedList = []
    #     if length < numberOfBreaks:
    #         print(-1)
    #     elif length % numberOfBreaks == 0:
    #         for i in range(numberOfBreaks):
    #             distributedList.append(length // numberOfBreaks)
    #     else:
    #         calculate = numberOfBreaks - (length % numberOfBreaks)
    #         final = length // numberOfBreaks
    #         for i in range(numberOfBreaks):
    #             if i >= calculate:
    #                 distributedList.append(final + 1)
    #             else:
    #                 distributedList.append(final)
    #
    #     distributedList.reverse()
    #
    #     return distributedList[index]
    #


#
if __name__ == '__main__':
    obj = UserInputPassword()
    obj.main_window()
