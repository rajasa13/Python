#Kalkulator v1.7.4

def kalkulator(numbers, operasi):
    hasil = numbers[0]
    for i in range(1, len(numbers)):
        if operasi == '+':
            hasil += numbers[i]
        elif operasi == '-':
            hasil -= numbers[i]
        elif operasi == '*':
            hasil *= numbers[i]
        elif operasi == '/':
            if numbers[i] != 0:
                hasil /= numbers[i]
            else:
                return "Error: Pembagian dengan Nol"
        else:
            return "Operasi bilangan salah"
    return int(hasil)

while True:
    numbers = []
    while True:
        num = input("Masukkan angka (atau masukkan 'q' untuk selesai): ")
        if num.lower() == 'q':
            break
        numbers.append(float(num))
    
    if not numbers:
        break
    operasi = input("Masukkan operasi bilangan (+, -, *, /): ")
    print(kalkulator(numbers, operasi))

    kalkulasi_lainnya = input("Apakah kamu ingin melakukan kalkulasi lainnya (ya/tidak)? ")
    if kalkulasi_lainnya.lower() ==  'tidak':
        break