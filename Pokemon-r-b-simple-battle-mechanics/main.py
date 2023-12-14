from createpokemondb import *
import threading as td
from user_classifier import *
import tkinter as tk
import pygame
import time


def main():
    pokemon_list = create_list_of_pokemon()
    player1 = Player('rico', 'Manual', pokemon_list)
    player1.select_pokemon(pokemon_list)
    player2 = Bot('bot', 'Auto', pokemon_list)
    player2.select_pokemon(pokemon_list, player1.pokemon)
    print(player1.pokemon.get_name())
    print(player2.pokemon.get_name())

    # Start the battle
    battle(player1, player2)

def battle(player1, player2):
    # Create the battle window
    battle_window = tk.Tk()
    battle_window.title('Battle')
    
    battle_window.geometry('600x400')
    player1_frame = tk.Frame(battle_window)
    player1_frame.pack(side=tk.BOTTOM)    
    player2_frame = tk.Frame(battle_window)     
    player2_frame.pack(side=tk.TOP)   
    player1_name = tk.Label(player1_frame, text=player1.pokemon.get_name())
    player1_name.pack()
 
    player2_name = tk.Label(player2_frame, text=player2.pokemon.get_name())
    player2_name.pack()

    pokemon1 = player1.pokemon
    pokemon2 = player2.pokemon
    
    health1_bar = tk.Canvas(player1_frame, width=100, height=20, bg='red')
    health1_bar.pack()
    health1_rect_id = health1_bar.create_rectangle(0, 0, 100, 20, fill='green')
    pokemon1_base_health = pokemon1.get_hp()
    #pokemon1 image
    pokemon1_png = tk.PhotoImage(file=pokemon1.get_png())
    pokemon1_image = tk.Label(player1_frame, image=pokemon1_png)
    pokemon1_image.pack()

    health2_bar = tk.Canvas(player2_frame, width=100, height=20, bg='red')
    health2_bar.pack()
    health2_rect_id =health2_bar.create_rectangle(0, 0, 100, 20, fill='green')
    #pokemon2 image
    pokemon2_png = tk.PhotoImage(file=pokemon2.get_png())
    pokemon2_image = tk.Label(player2_frame, image=pokemon2_png)
    pokemon2_image.pack()

    pokemon2_base_health = pokemon2.get_hp()
    
    print(f"Battle between {player1.pokemon.get_name()} and {player2.pokemon.get_name()}")
    def battle_loop():
        # make bar health pokemon 1
        health1 = pokemon1.get_hp()
        health1_percent = health1 / pokemon1_base_health
        health1_bar.coords(health1_rect_id, 0, 0, health1_percent * 100, 20)
        # make bar health pokemon 2 
        health2 = pokemon2.get_hp() 
        health2_percent = health2 / pokemon2_base_health
        health2_bar.coords(health2_rect_id, 0, 0, health2_percent * 100, 20)


        # Pokemon 1 attacks Pokemon 2
        if pokemon1.get_hp() <= 0:
            print(f"{pokemon1.get_name()} fainted!")
            health1_bar.coords(health1_rect_id, 0, 0, 0, 20)
            messagebox.showinfo('Battle', f'{pokemon1.get_name()} Fainted!')
            messagebox.showinfo('Battle', f'{pokemon2.get_name()} Wins!')
            return
        else:  
            player1.take_turn(pokemon2, battle_window)
        
        # Check if Pokemon 2 fainted
        if pokemon2.get_hp() <= 0:
            health2_bar.coords(health2_rect_id, 0, 0, 0, 20)
            print(f"{pokemon2.get_name()} fainted!")
            messagebox.showinfo('Battle', f'{pokemon2.get_name()} Fainted!')
            messagebox.showinfo('Battle', f'{pokemon1.get_name()} Wins!')
            return
        else:
        # Pokemon 2 attacks Pokemon 1
            player2.take_turn(pokemon1)

        # Check if Pokemon 1 fainted

        print(f"\n{pokemon1.get_name()} HP: {pokemon1.get_hp()} \ {pokemon2.get_hp()}\n")
        if health1 > 0 or health2 > 0:
            battle_window.after(1000, battle_loop)
        else:
            time.sleep(5)
            battle_window.destroy()
    battle_window.after(1000, battle_loop)
    battle_window.mainloop()

if __name__ == '__main__':
    main()
