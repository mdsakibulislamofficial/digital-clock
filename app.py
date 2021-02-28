import tkinter as tk
from tkinter import filedialog
from time import strftime


root = tk.Tk()
root.title("Clock")

root.resizable(0, 0)


def time():
    time_str = strftime('%I : %M : %S %p')
    label.config(text=time_str)
    label.after(1000, time)


label = tk.Label(root, font=("Orbitron", 70), bg="#000", fg="#00ffff", bd=30)
label.pack(anchor="center")
time()
root.mainloop()
