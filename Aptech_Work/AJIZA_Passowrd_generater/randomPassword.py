from tkinter import *
import random, string


class CheckBar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


class RandomPassword:
    password = ''

    def GeneratePassword(self, CheckList):
        SpecialCharacters = "@$-&.%!_#"
        if CheckList[0] == 1:
            self.password += ''.join(random.choice(string.ascii_lowercase) for i in range(3))
        if CheckList[1] == 1:
            self.password += ''.join(random.choice(string.ascii_uppercase) for i in range(3))
        if CheckList[2] == 1:
            self.password += ''.join(random.choice(string.digits) for i in range(3))
        if CheckList[3] == 1:
            self.password += ''.join(random.choice(string.ascii_letters) for i in range(3))
        if CheckList[4] == 1:
            self.password += ''.join(random.choice(SpecialCharacters) for i in range(3))

        return ''.join(random.choice(self.password) for i in range(15))

    def main_window(self):
        randomPasswordWindow = Tk()
        randomPasswordWindow.title("Random Password")
        app_width = 1000
        app_height = 600
        screen_width = randomPasswordWindow.winfo_screenwidth()
        screen_height = randomPasswordWindow.winfo_screenheight()
        x_cord = (screen_width / 2) - (app_width / 2)
        y_cord = (screen_height / 2) - (app_height / 2)
        randomPasswordWindow.geometry(f'{app_width}x{app_height}+{int(x_cord)}+{int(y_cord)}')
        randomPasswordWindow.resizable(0, 0)
        Output = Text(randomPasswordWindow, height=5,
                      width=25,
                      bg="white")

        lng = CheckBar(randomPasswordWindow, ['Lowercase', 'Uppercase', 'Numbers', 'Default', 'special characters'])
        lng.pack(side=TOP, fill=X)

        Output.insert(END, list(lng.state()))
        Output.pack()

        def checkCheckBox():
            Output.delete('1.0', END)
            Output.insert(END, self.GeneratePassword(list(lng.state())))

        Button(randomPasswordWindow, text='Peek', command=checkCheckBox).pack(side=RIGHT)

        randomPasswordWindow.mainloop()
