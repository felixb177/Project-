import csv
import os
import tkinter as tk
from tkinter import messagebox
from choose_seat import *
from choose_movie import *

def confirm_selection(username, password):
 global selected_option
 option = selected_option.get()
 messagebox.showinfo("Confirmation", f"You selected: {option}")
 if option == "choose_movie":
    choose_movie(username,password)
 if option == "look_at_ticket":
    pass

def menu(username, password):
    global selected_option
    window = tk.Tk()
    window.title("Choose")
    window.geometry("300x400")

    frame = tk.Frame(window)
    frame.pack(padx=50, pady=50)

    selected_option = tk.StringVar()

    rb1 = tk.Radiobutton(frame, text="Choose Movie", variable=selected_option, value="choose_movie")
    rb1.pack()

    rb2 = tk.Radiobutton(frame, text="Look at Ticket List", variable=selected_option, value="look_ticket_list")
    rb2.pack()

    confirm_button = tk.Button(window, text="Confirm", command=lambda: confirm_selection(username, password))
    confirm_button.pack(pady=20)
    
    window.mainloop()

menu('x','x')