#devloping password generator basic GUI
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.configure(bg = "black")
root.title("Password Generator")
root.minsize(600,175)
root.maxsize(600,175)
def center_window( width =600 , height = 175):
     #get screen width and height
     screen_width= root.winfo_screenwidth()
     screen_height= root.winfo_screenheight()
     #calculating the position of x and y coordinate
     x = (screen_width/2) - (width/2)
     y = (screen_height/2) - (height/2)
     root.geometry('%dx%d+%d+%d' % (width, height, x, y))
center_window()
def password_generator():

    uppercase= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase= "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    specical_char = "@#$%*/-^)(@@*))*\|"
    combination= lowercase + uppercase + numbers + specical_char
    global length , password;
    length1 = pass_length.get()
    if length1 > 66 :
        messagebox.showerror("Error" , "Password Length Value Exceeded")
    else:
        pass;
    password = "".join(random.sample(combination,length1))
    e.delete(0 ,END)
    e.insert(0,  password)
   
def copy():
    pyperclip.copy(password)
    messagebox.showinfo("successfull" , "Successfully copied to the clipboard")
def cls():
    e.delete(0, END)
def destroy():
    response = messagebox.askyesno("Exit", "Are you sure ?")
    if response is True:
        root.destroy
        ()
    else:
        pass;

mylabel = Label(root , text = "PASSWORD GENERATOR" , font =( "comic sans ms" , 25 ) , bg = "black",fg = "#29C0FF")
mylabel.pack()

pass_length = IntVar()
pass_length_label = Label(root , text = "Enter Password Length : ",fg = "#15FF28", bg = "black").pack()
length = Entry(root , textvariable = pass_length, width = 5 , bg = "white", fg = "black",cursor = "xterm #15FF28",).place(x = 380 , y = 55)
e = Entry(root , bg ="white" , fg = "green"  , selectbackground = "black",width = 40 ,borderwidth = 2 )
e.place( x = 198 ,y = 80)
mybutton2 = Button(root , text = "GENERATE PASSWORD" , command = password_generator , fg = "red", cursor = "hand2").place(x = 170 , y=110)
mybutton3 = Button(root , text = "Copy to Clipboard" , command = copy,fg = "red",cursor = "hand2" ).place(x = 330 , y=110)
mybutton4 = Button(root , text = "CLEAR" , command = cls,fg = "red" ,cursor = "hand2",padx = 32).place(x = 330 , y=140)
mybutton5 = Button(root , text = "QUIT" , command = destroy , fg = "red",cursor = "hand2" , padx = 48).place(x = 170 , y=140)


root.mainloop()

