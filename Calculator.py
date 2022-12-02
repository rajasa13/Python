#Kalkulator v1.6

pilih = input("""Selamat Datang Di Kalkulator v1.0
1. Tambah
2. Kurang
Pilihan: """)

if pilih == "Tambah" or pilih == "tambah":
    x = int(input("Masukkan angka pertama: "))
    y = int(input("Masukkan angka kedua: "))
    print("Hasilnya adalah " + str(x + y))
elif pilih == "Kurang" or pilih == "kurang":
    x = int(input("Masukkan angka pertama: "))
    y = int(input("Masukkan angka kedua: "))
    print("Hasilnya adalah " + str(x - y))
else:
    print("Error")
