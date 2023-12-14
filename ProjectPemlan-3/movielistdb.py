import csv
import os


def create_db():
  if not os.path.isfile('movielist.csv'):
    with open('movielist.csv', 'w') as csvfile:
      fieldnames = ['judul', 'director','rating']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
  else:
    print("File already exists")


if __name__ == "__main__":
  create_db()
