# TUGAS PENDAHULUAN #2 PROBLEM 3

# KAMUS
# nilai_x : int
# sudah_ketemu : bool
# batas_bawah : int
# batas_atas : int
# step : int
# digit : int
# angka_cantik : int

# ALGORITMA
# Deklarasi variabel
# Input user
nilai_x = int(input("Masukkan X: "))

# Boolean untuk mengetahui apakah angka cantik sudah ditemukan
sudah_ketemu = False

# Variabel untuk parameter iterasi for
batas_bawah = 1
batas_atas = 9
step = 1
digit = 1


# Iterasi
if nilai_x % 2 != 0 and nilai_x % 5 != 0:
    while not sudah_ketemu:  # Selagi angka cantik belum ditemukan
        for i in range(batas_bawah, batas_atas + 1, step):
            if i % nilai_x == 0 and not sudah_ketemu:
                angka_cantik = i
                sudah_ketemu = True  # Angka cantik sudah ditemukan, iterasi dihentikan

        if not sudah_ketemu:  # Iterasi for sudah selesai tapi masih belum ditemukan
            digit += 1  # Banyaknya digit pada parameter ditambah 1
            # Parameter pada iterasi disesuaikan dengan banyaknya digit yang ada pada nilai variabel digit
            batas_bawah = int("1"*digit) 
            batas_atas = int("9"*digit)
            step = int("1"*digit)
  
    # Output
    print(f"Bilangan cantik terkecil yang habis dibagi {nilai_x} ialah {angka_cantik}")

else:
    print("Input tidak valid")


 
