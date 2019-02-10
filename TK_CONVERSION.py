import tkinter as tk
root=tk.Tk()
root.config(bg="green")
from tkinter import messagebox

a=tk.Label(root,text=" To Convert Fahreniet to Celsius ").grid(row=0,column=1)
a1=tk.Entry(root)
a1.grid(row=0,column=2)
b=tk.Label(root,text="To Convert Celsius to Fahreniet ").grid(row=2,column=1)
b1=tk.Entry(root)
b1.grid(row=2,column=2)

def ans():
    a2=float(a1.get())
    b2=float(b1.get())
    x=(a2-32)*5/9
    y=(b2*9/5)+32
    messagebox.showinfo("Celsius",x)
    messagebox.showwarning("Fahreniet",y)
c=tk.Button(root, text="Submit",command=ans)
c.grid(row=3,column=2)
c.config(bg="red")
