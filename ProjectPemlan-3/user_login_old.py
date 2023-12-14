import csv


def login():
  print("Selamat datang di sistem login")
  with open("users.csv") as csvfile:
    database = csv.DictReader(csvfile)
    loggedin = False
    while not loggedin:
      username = input("Masukkan username: ")
      password = input("Masukkan password: ")
      for row in database:
        if row["username"] == username and row["password"] == password:
          print("Login berhasil!")
          loggedin = True
          break
      if not loggedin:
        print("Username atau password salah. Silakan coba lagi.")
        while True:
          print("1. Login Kembali")
          print("2. Register")
          choice = input()
          if choice == "1":
            login()
          elif choice == "2":
            register()
          else:
            break

    # Lanjutkan dengan program utama setelah login berhasil


def register():
  print("Silakan daftar untuk membuat akun baru")
  with open("users.csv", "a", newline="") as csvfile:
    fieldnames = ["username", "password"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    while True:
      username = input("Masukkan username baru: ")
      password = input("Masukkan password baru: ")
      if not any(row["username"] == username
                 for row in csv.DictReader(open("users.csv"))):
        writer.writerow({"username": username, "password": password})
        print("Akun berhasil dibuat!")
        break
      else:
        print("Username sudah digunakan. Silakan coba lagi.")
