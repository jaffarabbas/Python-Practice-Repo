from tkinter import *


class SplashScreen:
    splash_root = Tk()
    app_width = 1000
    app_height = 500
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()
    x_cord = (screen_width / 2) - (app_width / 2)
    y_cord = (screen_height / 2) - (app_height / 2)
    filename = PhotoImage(file="J:\\Program\\Github\\Python-Practice-Repo\\TkinterPractice\\images\\main_panel.png")

    def __init__(self):
        self.load_main_window()
        self.splash_root.after(2000, self.main_window)

    def load_main_window(self):
        self.splash_root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x_cord)}+{int(self.y_cord)}')
        self.splash_root.resizable(0, 0)
        background_label = Label(self.splash_root, image=self.filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.splash_root.overrideredirect(True)

        # splash screen label
        splash_label = Label(self.splash_root, text="AJIZA", bg="orange red", fg="white", font="none 24 bold")
        splash_label.config(anchor=CENTER)
        splash_label.pack()

    def main_window(self):
        self.splash_root.destroy()

        root = Tk()
        root.title("dashboad")
        root.geometry("3171x2098")


if __name__ == '__main__':
    splash = SplashScreen()
    mainloop()
