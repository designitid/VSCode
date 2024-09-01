print("================================================================")
print("=                 PROGRAM KALKULASI NILAI                      =")
print("================================================================")
print("= PROGRAM INI BERFUNGSI MENENTUKAN GRADE KELULUSAN NILAI ANDA  =")
print("============================START===============================")


nama = input("MASUKKAN NAMA ANDA: ")
nilai = int(input("MASUKKAN NILAI ANDA: "))
nim = int(input("MASUKKAN NIM ANDA: "))

if nilai < 80:
    if nilai > 75:
        print("Anda lulus mata kuliah dengan nilai C, {}!".format(nama))
    else:
        print("Maaf Anda harus mengulang mata kuliah di semester antara, {}!".format(nama))
elif nilai < 90:
    print("Selamat Anda lulus mata kuliah ini dengan nilai B, {}!".format(nama))
else:
    print("Selamat Anda lulus mata kuliah ini dengan nilai A, {}!".format(nama))


print("================================================================")
print('=         TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI          =')
print("================================================================")
print("================================================================")
print("=  JIKA ANDA MENGULANG MATA KULIAH MOHON HUBUNGI BIRO AKADEMIK =")
print("================================================================")