# PRAKTIKUM #1 PROBLEM 3

# KAMUS
# banyak_p : int
# banyak_e : int
# banyak_n : int
# banyak_g : int
# banyak_mobil : int

# ALGORITMA
# Input nilai banyak kelompok
banyak_p = int(input("Masukkan banyak kelompok P: "))
banyak_e = int(input("Masukkan banyak kelompok E: "))
banyak_n = int(input("Masukkan banyak kelompok N: "))
banyak_g = int(input("Masukkan banyak kelompok G: "))

# Deklarasi variabel banyak mobil
banyak_mobil = banyak_p  # Jumlah minimal yang diperlukan sama dengan banyak kelompok P

if banyak_e > 0:  # Percabangan untuk pembagian kelompok E
    if banyak_g >= banyak_e:
        banyak_mobil += banyak_e  # Penambahan mobil sama dengan banyak kelompok E
        banyak_g -= banyak_e  # Banyak kelompok G yang tersisa
    else:  # Banyak E lebih banyak dibanding G
        banyak_mobil += banyak_g  
        banyak_e -= banyak_g  # Banyak kelompok E yang tersisa
        banyak_g = 0  # Sudah terbagi semuanya
        banyak_mobil += banyak_e  # Penambahan mobil sama dengan banyak kelompok E sisa

if banyak_n > 0:  # Percabangan untuk pembagian kelompok N
    banyak_mobil += (banyak_n // 2)  # Pembagian kelompok N adalah dengan membagi dua
    if banyak_n % 2 != 0 and banyak_g > 0:  # Jika banyak N tidak habis dibagi 2 atau bersisa 1
        banyak_mobil += 1
        banyak_g -= 1  # Kelompok G terambil 1

if banyak_g > 0:  # Percabangan untuk pembagian kelompok G
    banyak_mobil += (banyak_g // 2)  # Pembagian kelompok G adalah dengan membagi 2

# Output banyak mobil yang dibutuhkan
print(f"Banyak mobil yang dibutuhkan adalah {banyak_mobil}")
