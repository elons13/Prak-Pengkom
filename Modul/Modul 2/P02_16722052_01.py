# PRAKTIKUM #2 PROBLEM 1
# Deskripsi : Program untuk mengetahui penjumlahan seluruh angka satuan halaman buku yang habis dibagi suatu bilangan

# KAMUS
# halaman, bilangan, sum, angka_satuan, digit : int
# selesai : bool

# ALGORITMA

# Deklarasi variabel
# Input user
halaman = int(input("Masukkan banyak halaman buku: "))
bilangan = int(input("Masukkan suatu bilangan: "))
sum = 0  # Penjumlahan seluruh angka satuan
angka_satuan = 0
digit = 0
selesai = False

while not selesai:
    angka_satuan += bilangan
    if angka_satuan <= halaman:
        digit = len(str(angka_satuan))  # Untuk mengetahui berapa banyak digit pada angka_satuan
        if digit == 1:
            sum += angka_satuan
        else:
            sum += angka_satuan % 10
    else:
        selesai = True

print(f"Hasil penjumlahannya adalah {sum}")
