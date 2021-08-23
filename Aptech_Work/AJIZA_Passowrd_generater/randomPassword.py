from tkinter import *
import random, string
from copyPassword import CopyPassword
import dashboard


class RandomPassword:
    password = ''
    checkValue = []
    PasswordLength = 0

    def main_window(self):
        # variables
        randomPasswordWindow = Tk()
        randomPasswordWindow.title("Random Password")
        app_width = 1000
        app_height = 600
        LengthValue = IntVar()
        LengthValue.set(15)
        self.PasswordLength = LengthValue.get()
        varValueForCheckBox = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        screen_width = randomPasswordWindow.winfo_screenwidth()
        screen_height = randomPasswordWindow.winfo_screenheight()
        x_cord = (screen_width / 2) - (app_width / 2)
        y_cord = (screen_height / 2) - (app_height / 2)
        RandomPasswordBackgroundImage = PhotoImage(file="images/randomPasswordBackground.png")
        copyGeneratedPassword = PhotoImage(file="images/CopyPasswordButton.png")
        generatePasswordButton = PhotoImage(file="images/passwordGenerateButton.png")
        checkBeforeImage = PhotoImage(file="images/Checkbox.png")
        checkAfterImage = PhotoImage(file="images/checked.png")
        backButtonImage = PhotoImage(file="images/back.png")

        background_label = Label(randomPasswordWindow, image=RandomPasswordBackgroundImage)
        CopyGeneratedPassword = copyGeneratedPassword.subsample(3, 3)
        GeneratePasswordButton = generatePasswordButton.subsample(3, 3)
        BackButton = backButtonImage.subsample(3, 3)

        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        randomPasswordWindow.resizable(0, 0)
        randomPasswordWindow.geometry(f'{app_width}x{app_height}+{int(x_cord)}+{int(y_cord)}')

        def backToDashboard():
            backObject = dashboard.Dashboard()
            randomPasswordWindow.destroy()
            backObject.main_window()

        BackToDashboardButton = Button(randomPasswordWindow, image=BackButton, compound=LEFT, bg='white',
                                       borderwidth=0, command=backToDashboard)
        BackToDashboardButton.place(x=14, y=10)

        Output = Text(randomPasswordWindow, height=1, borderwidth=0,
                      width=40,
                      bg="white", font=("Corbel", 25))

        Output.place(x=122, y=219)

        CheckBox_1 = Checkbutton(randomPasswordWindow, variable=varValueForCheckBox[0], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=260, y=350)
        CheckBox_2 = Checkbutton(randomPasswordWindow, variable=varValueForCheckBox[1], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=565, y=350)
        CheckBox_3 = Checkbutton(randomPasswordWindow, variable=varValueForCheckBox[2], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=838, y=350)
        CheckBox_4 = Checkbutton(randomPasswordWindow, variable=varValueForCheckBox[3], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=220, y=395)
        CheckBox_5 = Checkbutton(randomPasswordWindow, variable=varValueForCheckBox[4], onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=630, y=395)

        # text field for password length
        Length = Entry(borderwidth=0, width=12, font=("Segoe UI", 14), textvariable=LengthValue)
        Length.place(x="822", y="394")

        def state():
            self.checkValue.clear()
            for i in varValueForCheckBox:
                self.checkValue.append(int(i.get()))
            return self.checkValue

        def Copy():
            CopyPassword.CopyPassword(Output.get("1.0", END))

        CopyButton = Button(randomPasswordWindow, image=CopyGeneratedPassword, compound=LEFT, bg='white', borderwidth=0,
                            command=Copy)
        CopyButton.place(x=830, y=209)

        def checkCheckBox():
            Output.configure(state="normal")
            self.password = ''
            Output.delete('1.0', END)
            Output.insert(END, self.GeneratePassword(list(state())))
            Output.configure(state='disabled')
            self.PasswordLength = LengthValue.get()

        GenerateButton = Button(randomPasswordWindow, image=GeneratePasswordButton, compound=LEFT, bg='white',
                                borderwidth=0, command=checkCheckBox)
        GenerateButton.place(x=300, y=450)
        randomPasswordWindow.mainloop()

    def GeneratePassword(self, CheckList):
        SpecialCharacters = "@$-&.%!_#"
        try:
            if CheckList[0] == 1:
                self.password += ''.join(random.choice(string.ascii_lowercase) for i in
                                         range(self.LengthDistribution(self.PasswordLength, 4, 0)))
            if CheckList[1] == 1:
                self.password += ''.join(random.choice(string.ascii_uppercase) for i in
                                         range(self.LengthDistribution(self.PasswordLength, 4, 1)))
            if CheckList[2] == 1:
                self.password += ''.join(random.choice(string.digits) for i in
                                         range(self.LengthDistribution(self.PasswordLength, 4, 2)))
            if CheckList[3] == 1:
                self.password += self.GenerateDefaultPassword()
            if CheckList[4] == 1:
                self.password += ''.join(random.choice(SpecialCharacters) for i in
                                         range(self.LengthDistribution(self.PasswordLength, 4, 3)))
            if CheckList.count(0) == 5:
                print("Error")

        except EXCEPTION:
            print(EXCEPTION)

        return ''.join(random.choice(self.password) for i in range(self.PasswordLength))

    # generate random password by default
    def GenerateDefaultPassword(self):
        SpecialCharacters = "@$-&.%!_#"
        randomLowerString = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
        randomUpperString = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
        randomDigit = ''.join(random.choice(string.digits) for i in range(4))
        randomSpecialString = ''.join(random.choice(SpecialCharacters) for i in range(3))
        tempPassword = randomLowerString + randomUpperString + randomSpecialString + randomDigit
        return ''.join(random.choice(tempPassword) for i in range(len(tempPassword)))

    # distribute password length
    def LengthDistribution(self, length, numberOfBreaks, index):
        distributedList = []
        if length < numberOfBreaks:
            print(-1)
        elif length % numberOfBreaks == 0:
            for i in range(numberOfBreaks):
                distributedList.append(length // numberOfBreaks)
        else:
            calculate = numberOfBreaks - (length % numberOfBreaks)
            final = length // numberOfBreaks
            for i in range(numberOfBreaks):
                if i >= calculate:
                    distributedList.append(final + 1)
                else:
                    distributedList.append(final)

        distributedList.reverse()

        return distributedList[index]


#
if __name__ == '__main__':
    obj = RandomPassword()
    obj.main_window()
