import tkinter as tk
root=tk.Tk()
root.config(bg="green")
from tkinter import messagebox

a=tk.Label(root,text=" User ID : ").grid(row=0,column=1)
a1=tk.Entry(root)
a1.grid(row=0,column=2)
b=tk.Label(root,text="password").grid(row=2,column=1)
b1=tk.Entry(root)
b1.grid(row=2,column=2)

def ans():
    a2=a1.get()
    b2=b1.get()
    if (a2=="ram" and b2=="sita"):
        messagebox.showinfo('massage','Login Successful')
    elif(a2=="ram"):
        messagebox.showerror("error ","sorry Password Incorrect")
    elif(b2=="sita"):  
        messagebox.showwarning('wornig','User ID Incorrect')
        
c=tk.Button(root, text="Submit",command=ans)
c.grid(row=3,column=2)
c.config(bg="red")

