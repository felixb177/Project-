import csv
import os
import tkinter as tk
from tkinter import messagebox
from choose_seat import choose_seat_window
def load_movies():
 with open('movielist.csv', 'r') as csvfile:
     reader = csv.DictReader(csvfile)
     movies = [row['judul'] for row in reader]
     print(movies)
 return movies

def confirm_selection(window, username, password, movie_vars):
    print(movie_vars)
    selected_movie = movie_vars.get()
    print(selected_movie)
    
    messagebox.showinfo("Confirmation", f"You selected: {selected_movie}")
    window.destroy()
    choose_seat_window(selected_movie, username ,password)

def choose_movie_window(username, password):
 global movie_vars
 window = tk.Tk()
 
 window.title("Movie Selection")
 window.geometry("300x400")

 frame = tk.Frame(window)
 frame.pack(padx=50, pady=50)

 movies = load_movies()
 movie_vars = tk.StringVar()
 for movie in movies:
     rb = tk.Radiobutton(frame, text=movie, variable=movie_vars, value=movie)
     rb.pack(anchor=tk.W)

 confirm_button = tk.Button(window, text="Confirm", command=lambda: confirm_selection(window, username, password, movie_vars))
 confirm_button.pack(pady=20)

 window.mainloop()
 return movie_vars

