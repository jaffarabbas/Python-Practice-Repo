import pyperclip


class CopyPassword:
    @staticmethod
    def CopyPassword(value):
        pyperclip.copy(value)
