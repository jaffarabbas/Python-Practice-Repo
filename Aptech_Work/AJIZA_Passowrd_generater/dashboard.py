from tkinter import *
from randomPassword import RandomPassword
from userInputPassword import UserInputPassword


class Dashboard:
    def main_window(self):
        dashboard = Tk()
        dashboard.title("Dashboard")
        app_width = 1000
        app_height = 600
        screen_width = dashboard.winfo_screenwidth()
        screen_height = dashboard.winfo_screenheight()
        x_cord = (screen_width / 2) - (app_width / 2)
        y_cord = (screen_height / 2) - (app_height / 2)
        dashboardImage = PhotoImage(file="images/dashboard.png")
        randomButtonImage = PhotoImage(file="images/randomPasswordButton.png")
        userInputButtonImage = PhotoImage(file="images/userInputPassword.png")
        dashboard.geometry(f'{app_width}x{app_height}+{int(x_cord)}+{int(y_cord)}')
        background_label = Label(dashboard, image=dashboardImage)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        dashboard.resizable(0, 0)
        RandomBtnImage = randomButtonImage.subsample(3, 3)
        UserInputBtnImage = userInputButtonImage.subsample(3, 3)

        def OpenRandomPasswordScreen():
            dashboard.destroy()
            randomPasswordScreen = RandomPassword()
            randomPasswordScreen.main_window()

        def OpenUserInputPasswordScreen():
            dashboard.destroy()
            userInputPassword = UserInputPassword()
            userInputPassword.main_window()

        Button(dashboard, image=RandomBtnImage, compound=LEFT, bg='white', borderwidth=0,
               command=OpenRandomPasswordScreen).place(x=600, y=200)
        Button(dashboard, image=UserInputBtnImage, compound=LEFT, bg='white', borderwidth=0,
               command=OpenUserInputPasswordScreen).place(x=580, y=350)

        dashboard.mainloop()
