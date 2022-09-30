# TUGAS PENDAHULUAN #2 PROBLEM 2

# KAMUS
# nilai_a : int
# nilai_b : int
# banyak_prima : int
# prima_terbesar : int
# prima : bool
# kondisi_khusus : bool

# ALGORITMA
nilai_a = int(input("Masukkan a: "))
nilai_b = int(input("Masukkan b: "))

# Deklarasi variabel untuk banyaknya bilangan prima dan bilangan prima terbesar
banyak_prima = 0
prima_terbesar = 0
kondisi_khusus = False  # Kondisi khusus untuk bilangan 2

if nilai_a > 0 and nilai_b >= nilai_a:  # Supaya bisa berjalan

    # Khusus untuk bilangan 2, pada rentang yang hanya memuat 1 atau 2
    if nilai_a == 2 or nilai_b == 2:  # Dipastikan ada 1 bilangan prima yaitu 2
       banyak_prima += 1
       prima_terbesar = 2
       kondisi_khusus = True

    # Tujuan berikutnya adalah mencari bilangan yang bukan prima, pada rentang yang tidak hanya memuat 1 atau 2
    if nilai_a >= 3 or nilai_b >= 3:  
        for i in range(nilai_a, nilai_b + 1):
            if i == 1:
                prima = False  # 1 bukan bilangan prima
            elif kondisi_khusus:
                prima = False
            else:
                prima = True  # Asumsi i merupakan prima

            kondisi_khusus = False  # Mengubah kembali nilai variabel menjadi False supaya conditional hanya berjalan sekali

            # Looping untuk mengecek apakah ada bilangan yang habis membagi
            for j in range(2, nilai_b + 1):
                if i != j:  # Jika i tidak sama dengan j, maka tidak boleh habis membagi
                    if i % j == 0:  # Dipastikan bukan bilangan prima
                        prima = False

            if prima:
                banyak_prima += 1  # Nilai variabel bertambah 1
                prima_terbesar = i  # Mengganti nilai variabel dengan nilai yang baru

    # Output
    if banyak_prima == 0:
        print(f"Tidak ditemukan adanya bilangan prima pada selang [{nilai_a},{nilai_b}].")
    else:
        print(f"Banyaknya bilangan prima pada selang [{nilai_a},{nilai_b}] adalah {banyak_prima}. Bilangan prima terbesar di selang tersebut adalah {prima_terbesar}")
else:
    print("Input yang dimasukkan tidak valid")