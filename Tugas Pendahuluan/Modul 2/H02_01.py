# TUGAS PENDAHULUAN #2 PROBLEM 1

# KAMUS
# nilai_n : int
# nilai_a : int
# nilai_b : int
# nilai_c : int
# habis_a : str
# habis_b : str
# habis_c : str
# habis : bool

# ALGORITMA
# Deklarasi variabel
nilai_n = int(input("Masukkan nilai N: "))
nilai_a = int(input("Masukkan nilai A: "))
nilai_b = int(input("Masukkan nilai B: "))
nilai_c = int(input("Masukkan nilai C: "))

# Loop for untuk setiap elemen dari 1 hingga N
for x in range(1, nilai_n + 1):

    # Deklarasi variabel tambahan untuk looping for
    habis_a = ""
    habis_b = ""
    habis_c = ""
    habis = False

    if x % nilai_a == 0:
        habis_a = "Siap"
        habis = True
    if x % nilai_b == 0:
        habis_b = "Bang"
        habis = True
    if x % nilai_c == 0:
        habis_c = "Jago"
        habis = True
    # Sampai sini, sudah tersimpan kata apa saja yang akan keluar

    # Percabangan ini untuk mengetahui untuk setidaknya ada 1 kondisi yang benar
    if habis:
        print(habis_a + habis_b + habis_c, end=" ")
    else:
        print(x, end=" ")

