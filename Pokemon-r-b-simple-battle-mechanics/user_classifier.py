import random
import time
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox
class User(ABC):
    def __init__(self, name, control, pokemon):
        self.name = name
        self.control = control
        self.pokemon = pokemon
    @abstractmethod
    def select_pokemon(self, pokemon):
        self.pokemon = pokemon
    @abstractmethod
    def take_turn(self):
        pass
class Player(User):
    def __init__(self, name = 'Player', control = 'Manual', pokemon = None):
        super().__init__(name, control, pokemon)
        self.move_selected = None
    def select_pokemon(self, pokemon_list):
        window = tk.Tk()
        window.title('Pokemon Selection')
        window.geometry('500x500')

        frame = tk.Frame(window)
        frame.pack(padx=50, pady=50)

        label = tk.Label(frame, text='Select your pokemon')
        label.pack()
        
        selected_pokemon = tk.Listbox(frame)
        selected_pokemon.pack(anchor=tk.W)

        for i,pokemon in enumerate(pokemon_list):
            temp_list = []
            temp_list.append(pokemon.get_name())
            selected_pokemon.insert(i, pokemon.get_name())

        def on_select():
            index = selected_pokemon.curselection()[0]  # Get the index of the selected Pokemon
            self.pokemon = pokemon_list[index]
            window.destroy()

        select_button = tk.Button(frame, text="Select", command=on_select)
        select_button.pack()
        window.mainloop()

    def take_turn(self,other_pokemon, battle_window):
        self.move_selected = tk.BooleanVar(value=False)
        moves_list = self.pokemon.get_Skills()
        frame = tk.Frame(battle_window)
        frame.pack(side=tk.BOTTOM, anchor=tk.SE)
        selected_move = tk.Listbox(frame)
        selected_move.pack(anchor=tk.W)
        for i, move in enumerate(moves_list):
            temp_list = []
            temp_list.append(move.get_name())
            selected_move.insert(i, move.get_name())
        def on_select():
            index = selected_move.curselection()[0]
            mymove = moves_list[index]
            messagebox.showinfo('Select move', f"you selected {mymove.get_name()}!")
    
            self.pokemon.attack(other_pokemon,mymove)
            self.move_selected.set(True)
        
        select_button = tk.Button(frame, text="Select", command=on_select)
        select_button.pack()
        frame.tkraise()
        battle_window.update()
        frame.wait_variable(self.move_selected)

        frame.destroy()
        

            
        
        
class Bot(User):
    def __init__(self, name = 'Bot', control = 'Auto', pokemon = None):
        super().__init__(name, control, pokemon)
    def select_pokemon(self, pokemon_list, other_pokemon):
        self.pokemon = random.choice(pokemon_list)
        while self.pokemon == other_pokemon:
            self.pokemon = random.choice(pokemon_list)
    def take_turn(self, other_pokemon):
        move = random.choice(self.pokemon.get_Skills())
        self.pokemon.attack(other_pokemon, move)

# pokemon_list = create_list_of_pokemon()
# player1 = Player('rico', 'Manual', pokemon_list)
# player1.select_pokemon(pokemon_list)
# name = player1.pokemon.get_hp()
# print(name)