#calculator python by DANI ANTO PAKPAHAN
#232406083
#B-1/TEKNIK INFORMATIKA 2023

#Penjumlahan
def add(x, y):
    return x + y

#Pengurangan
def subtract(x, y):
    return x - y

#Perkalian
def multiply(x, y):
    return x * y

# Pembagian
def divide(x, y):
    if y == 0:
        return "0"
    if x == 0:
        return "0"
    return x / y

num1 = float(input("Masukkan Angka Pertama: "))
num2 = float(input("Masukkan Angka Ke Dua: "))

print("Pilih Layanan Operasi yang Di Inginkan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choice = input("Pilih Operasi (1/2/3/4): ")

if choice == '1':
    print("Jawaban: ", add(num1, num2))
elif choice == '2':
    print("Jawaban: ", subtract(num1, num2))
elif choice == '3':
    print("Jawaban: ", multiply(num1, num2))
elif choice == '4':
    print("Jawaban: ", divide(num1, num2))
else:
    print("Operasi tidak ada dalam pilihan, pilih angka 1-4 dan jalankan program ulang")


