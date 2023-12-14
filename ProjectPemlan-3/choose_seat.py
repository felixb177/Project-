import csv
import tkinter as tk
from tkinter import messagebox

def choose_seat_window(selected_movie, username, password):
    print(selected_movie)
    filename = '{}.csv'.format(selected_movie)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        seats = list(reader)

        root = tk.Tk()
        seat_buttons = [[None for _ in range(len(seats[0]))] for _ in range(len(seats))]
        cart = []  # Keranjang untuk menyimpan informasi kursi yang ditekan

        # Create a Seat Selection GUI
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                text = seats[i][j]
                seat_buttons[i][j] = tk.Button(root, text=text, command=lambda i=i, j=j: book_seat(seats, selected_movie, seat_buttons, i, j, cart))
                seat_buttons[i][j].grid(row=i, column=j)

        def save_and_confirm():
            confirmation = messagebox.askokcancel("Confirm", "Are you sure you want to confirm? Changes will be saved.")
            if confirmation:
                save_data(selected_movie, seats)
                save_cart(cart, selected_movie, username, password)  # Simpan keranjang ke file CSV
                root.destroy()
                messagebox.showinfo("Confirmation", "Your seat has been booked!")
       

        confirm_button = tk.Button(root, text="Confirm", command=save_and_confirm)
        confirm_button.grid(row=len(seats) + 1, columnspan=len(seats[0]))  # Place the Confirm button below the seats

        def on_closing():
            if messagebox.askokcancel("Confirm", "Are you sure you want to close? Changes will be saved."):
                root.destroy()
                save_data(selected_movie, seats)
          
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

def save_data(selected_movie, seats):
    with open('{}.csv'.format(selected_movie), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(seats)

# Save Cart to CSV
def save_cart(cart, selected_movie, username, password):
    with open('users.csv', 'a', newline='') as file:  # 'a' means append mode
        writer = csv.writer(file)
        for seat in cart:
            writer.writerow([username, password, selected_movie, seat])  # Menulis data

# Handle Seat Selection
def book_seat(seats, selected_movie, seat_buttons, i, j, cart):
    seats[i][j] = 'X'
    seat_buttons[i][j].config(text='X')  # Update the button's text
    cart.append((i, j))  # Tambahkan informasi kursi ke keranjang

