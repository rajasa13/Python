#Kalkulator v1.7

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

num1 = float(input("Masukkan angka pertama: "))
operasi = input("Masukkan operasi bilangan (+, -, *, /): ")
num2 = float(input("Masukkan angka kedua: "))

print(kalkulator(num1, operasi, num2))