import tkinter as tk
import csv
from tkinter import messagebox
from choose_movie import choose_movie_window
import time


def see_ticket_list(username, password):
 with open('users.csv', 'r') as csvfile:
   reader = csv.DictReader(csvfile)
   tickets = []
   for row in reader:
     if row['username'] == username and row['password'] == password:
       tickets.append(f"Movie: {row['tiket_film']}\nSeat: {row['jumlah']}")
   if not tickets:
     messagebox.showerror("Ticket List", "You haven't booked any tickets yet!")
   else:
     messagebox.showinfo("Ticket List", "\n".join(tickets))


def confirm_selection(window, username, password):
 global selected_option
 option = selected_option.get()
 
 messagebox.showinfo("Confirmation", f"You selected: {option}")
 
 if option == "choose_movie":
   window.destroy()
   choose_movie_window(username,password)
 if option == "look_ticket_list":
   #add see ticket list

   see_ticket_list(username, password)
 
 ##belum seleesai ya
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

    confirm_button = tk.Button(window, text="Confirm", command=lambda: confirm_selection(window,username, password))
    confirm_button.pack(pady=20)
    
    window.mainloop()
    
#menu('x','x')