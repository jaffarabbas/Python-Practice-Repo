from tkinter import *
from tkinter import ttk

window = Tk()
EntryList = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(window, "1")]
file = open('data.txt', 'a')

window.title("Registration")
window.geometry('400x400')
window.configure(background = "grey");
a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
d = Label(window ,text = "Address").grid(row = 3,column = 0)
d = Label(window ,text = "gender").grid(row = 4,column = 0)

a1 = Entry(window, textvariable=EntryList[0]).grid(row = 0,column = 1)
b1 = Entry(window, textvariable=EntryList[1]).grid(row = 1,column = 1)
c1 = Entry(window, textvariable=EntryList[2]).grid(row = 2,column = 1)
d1 = Entry(window, textvariable=EntryList[3]).grid(row = 3,column = 1)
# Dictionary to create multiple buttons
values = {"Male": "Male",
          "Female": "Female"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
count = 0
for (text, value) in values.items():
   Radiobutton(window, text=text, variable=EntryList[4],value=value).grid(row = (count+4),column = 1)
   count+=1


def SendData():
   for i in EntryList:
      print(i.get())
      file.write(i.get()+'\n')
   file.close()

def DataShow():
   reader = open('data.txt','r')
   print(reader.read())

btn = ttk.Button(window,command=SendData,text="Submit").grid(row=6,column=0)
btn = ttk.Button(window,command=DataShow,text="Read").grid(row=7,column=0)


window.mainloop()