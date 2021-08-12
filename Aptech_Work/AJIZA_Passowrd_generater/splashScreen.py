from tkinter import *
from dashboard import Dashboard


class SplashScreen:
    splash_root = Tk()
    app_width = 1000
    app_height = 600
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x_cord = (screen_width / 2) - (app_width / 2)
    y_cord = (screen_height / 2) - (app_height / 2)
    splashImage = PhotoImage(file="images/splash.png")
    dashboard = Dashboard()

    def __init__(self):
        self.load_main_window()
        self.splash_root.after(100, self.main_window)

    def load_main_window(self):
        self.splash_root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x_cord)}+{int(self.y_cord)}')
        self.splash_root.resizable(0, 0)
        background_label = Label(self.splash_root, image=self.splashImage)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.splash_root.overrideredirect(True)

    def main_window(self):
        self.splash_root.destroy()
        self.dashboard.main_window()
