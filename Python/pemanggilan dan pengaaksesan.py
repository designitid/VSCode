hewan = ["ayam", "anjing", "ikan", "udang"]
print(hewan)
print(hewan[0], hewan[-2])#mengakses list
print(hewan[::-1]) #membalikkan list
print(hewan[1:3])#mengambil bagian
print(hewan[::3])#mengambil langkahan (step)

#pengoperasian
hewan[1] = "Kucing" #mengubah list
hewan.append("kuda")#menambah elemen di akhir
hewan.insert(1,"paus")#menambah elemen di indeks 1
hewan.remove("ikan")#menghapus elemen ikan
hewan.pop(3)#menghapus elemen di index 5
hewan = hewan + ["Semut", "Lebah"]#menggabungkan list
#hewan.clear()#menghapus list
print(hewan)#menampilkan isi list

#pengecekan
print("anjing" in hewan)