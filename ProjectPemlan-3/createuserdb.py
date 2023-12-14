import csv
import os


def create_db():
  if not os.path.isfile('users.csv'):
    with open('users.csv', 'w') as csvfile:
      fieldnames = ['username', 'password','tiket_film','jumlah']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
  else:
    print("File already exists")


if __name__ == "__main__":
  create_db()
