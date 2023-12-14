import os
import csv
import tkinter as tk

class Movie():
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
        with open("movielist.csv", "a", newline="") as csvfile:
            fieldnames = ['judul', 'director', 'rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'judul': title, 'director': director,'rating':rating})
            print("film berhasil ditamabhkan ke data base")

        filename = '{}.csv'.format(self.title)
        if not os.path.isfile(filename):
            
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['A', 'B', 'C']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for index in range(1, 11):
                    row = {'A': '1', 'B': '1', 'C': '1'}
                    writer.writerow(row)
        else:
            print("File already exists")


if __name__ == "__main__":
    barbie = Movie(title="barbie", director="ocir", rating="9.6")
    spidey = Movie(title="spidey", director="tomas", rating="6.9")
    goat_documentary = Movie(title="goat_documentary", director="obryan jamesons", rating="9.9")
    