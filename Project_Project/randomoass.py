from tkinter import *
root = Tk()

lbl=Label(root, text="THIS IS LABEL WIDGET", fg='#B81376', font=("Corbel 25 underline"))
lbl.place(x=350, y=20)

lbl2=Label(root, text="Below are characters which will be added to password after checked", fg='#B81376', font=("Corbel 20"))
lbl2.place(x=150, y=100)

lbl5=Entry(root, width=50, fg='#B81376', font=("Segoe 15 bold"))
lbl5.place(x=250, y=170)

lbl3=Label(root, text="CHARACTERS", fg='#B81376', font=("Corbel 25 bold"))
lbl3.place(x=400, y=230)

chk1=Checkbutton(root, text="UPPER CASE", fg='#B81376', font=("Corbel 15 bold"))#.grid(row=10, column=0)
chk1.place(x=90, y=300)
chk2=Checkbutton(root, text="LOWER CASE", fg='#B81376', font=("Corbel 15 bold"))#.grid(row=10, column=1)
chk2.place(x=390, y=300)
chk3=Checkbutton(root, text="NUMBER", fg='#B81376', font=("Corbel 15 bold"))#.grid(row=10, column=2)
chk3.place(x=700, y=300)
chk4=Checkbutton(root, text="DEFAULT", fg='#B81376', font=("Corbel 15 bold"))#.grid(row=12, column=0)
chk4.place(x=90,y=380)
chk5=Checkbutton(root, text="SPECIAL CHARACTERS", fg='#B81376', font=("Corbel 15 bold"))#.grid(row=12, column=0)
chk5.place(x=390,y=380)
lbl4=Label(root, text="LENGTH", fg='#B81376', font=("Corbel 15 bold"))#.grid(row=12, column=1)
lbl4.place(x=700, y=380)
lb4=Entry(root)#.grid(row=12, column=2)
lb4.place(x=790, y=385)

btn=Button(root, text="GENERATE", bg='#A9176F', fg= '#ffffff', bd=10, font=("Corbel 15 bold"))#.grid(row=9, column=1)
btn.place(x=440, y=450)

root.geometry("1000x600")
root.mainloop()