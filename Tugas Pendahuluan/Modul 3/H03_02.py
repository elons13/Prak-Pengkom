# TUGAS PENDAHULUAN #3 PROBLEM 2
# Deskripsi : Program untuk mengetahui apakah ada nilai yang sama dari bilangan-bilangan yang diinput user

# KAMUS
# banyak : int
# list_angka : list
# sama : bool

# ALGORITMA
# Input user
banyak = int(input("Masukkan N: "))

# List kosong untuk menyimpan angka yang dimasukkan oleh user
list_angka = [0 for i in range(banyak)]
# Boolean untuk mengetahui apakah ada yang sama dari sekumpulan bilangan tersebut
sama = False

# Iterasi untuk memasukkan nilai yang diinput user ke dalam list_angka
for i in range(banyak):
    angka = int(input(f"Masukkan bilangan ke {i + 1}: "))
    list_angka[i] = angka

# Mengecek apakah ada yang sama
for i in range(banyak):
    for j in range(banyak):
        if i != j and list_angka[i] == list_angka[j]:  # Harus dipastikan kedua nilai yang sedang dibandingkan tidak memiliki indeks yang sama
            sama = True

# Output
if sama:
    print("Tidak berbeda semua")
else:
    print("Berbeda semua")
