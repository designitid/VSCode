def cek_kelulusan(nilai):

  if nilai >= 80:
    if nilai >= 90:
      return "Lulus, predikat A"
    elif nilai >= 80:
      return "Lulus, predikat B"
    else:
      return "Lulus, predikat C"
  else:
    return "Gagal"

def main():
  nama_siswa = []
  nilai_ujian = []
  while True:
    nama = input("Masukkan nama siswa (enter untuk berhenti): ")
    if nama == "":
      break
    nilai = float(input("Masukkan nilai ujian siswa: "))
    nama_siswa.append(nama)
    nilai_ujian.append(nilai)

  status_kelulusan = []
  for nama, nilai in zip(nama_siswa, nilai_ujian):
    status_kelulusan.append(cek_kelulusan(nilai))

  nilai_rata_rata = sum(nilai_ujian) / len(nama_siswa)

  for i in range(len(nama_siswa)):
    print("Nama: {} | Status: {} ({})".format(nama_siswa[i], status_kelulusan[i], nilai_ujian[i]))
  print("Nilai rata-rata kelas:", nilai_rata_rata)


if __name__ == "__main__":
  main()
