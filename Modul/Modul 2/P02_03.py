# PRAKTIKUM #2 PROBLEM 3
# Deskripsi : Program untuk mengetahui banyaknya digit K yang muncul dari setiap halaman yang telah dibaca

# KAMUS
# halaman_pertama, halaman_terakhir, nilai_k, banyak : int

# ALGORITMA
halaman_pertama = int(input("Masukkan halaman pertama: "))
halaman_terakhir = int(input("Masukkan halaman terakhir: "))
nilai_k = int(input("Masukkan K: "))
banyak = 0

for halaman in range(halaman_pertama, halaman_terakhir+1):
    for angka in str(halaman):
        if int(angka) == nilai_k:
            banyak += 1

print(f"Digit {nilai_k} muncul sebanyak {banyak} kali")
