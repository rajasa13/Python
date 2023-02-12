#Kalkulator v1.7.1

def kalkulator(num1, operasi, num2):
    if operasi == '+':
        return num1 + num2
    elif operasi == '-':
        return num1 - num2
    elif operasi == '*':
        return num1 * num2
    elif operasi == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Pembagian dengan Nol"
    else:
        return "Operasi bilangan salah"

while True:
    num1 = float(input("Masukkan angka pertama: "))
    operasi = input("Masukkan operasi bilangan (+, -, *, /): ")
    num2 = float(input("Masukkan angka kedua: "))

    print(kalkulator(num1, operasi, num2))
    kalkulasi_lainnya = input("Apakah kamu ingin melakukan kalkulasi lainnya (ya/tidak)? ")
    if kalkulasi_lainnya.lower() ==  'tidak':
        break