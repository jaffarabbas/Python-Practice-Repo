from tkinter import *

top = Tk()
top.geometry("500x500")
CheckBox_1 = Checkbutton(top, variable=varValueForCheckBox, onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=260, y=350)

        CheckBox_2 = Checkbutton(, variable=varValueForCheckBox2, onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=565, y=350)
        CheckBox_3 = Checkbutton(, variable=varValueForCheckBox, onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=838, y=350)
        CheckBox_4 = Checkbutton(, variable=varValueForCheckBox, onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=220, y=395)
        CheckBox_5 = Checkbutton(, variable=varValueForCheckBox, onvalue=1, offvalue=0, height=0,
                                 width=0, bg="white",
                                 image=checkBeforeImage,
                                 selectimage=checkAfterImage, indicatoron=False, borderwidth=0, ).place(x=630, y=395)
        self.checkValue.append(varValueForCheckBox2)

top.mainloop()


