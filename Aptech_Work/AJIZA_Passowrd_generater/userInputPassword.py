from tkinter import *


class UserInputPassword:

    def main_window(self):
        randomPasswordWindow = Tk()
        randomPasswordWindow.title("UserInput Password")
        app_width = 1000
        app_height = 600
        screen_width = randomPasswordWindow.winfo_screenwidth()
        screen_height = randomPasswordWindow.winfo_screenheight()
        x_cord = (screen_width / 2) - (app_width / 2)
        y_cord = (screen_height / 2) - (app_height / 2)
        randomPasswordWindow.geometry(f'{app_width}x{app_height}+{int(x_cord)}+{int(y_cord)}')
        randomPasswordWindow.resizable(0, 0)

        randomPasswordWindow.mainloop()
