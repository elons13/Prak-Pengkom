# PRAKTIKUM #1 PROBLEM 2

# KAMUS
# nilai_a : float
# nilai_b : float
# nilai_c : float
# diskriminan : float

# ALGORITMA
# Input nilai A, B, dan C
nilai_a = float(input("Masukkan nilai A: "))
nilai_b = float(input("Masukkan nilai B: "))
nilai_c = float(input("Masukkan nilai C: "))

diskriminan = nilai_b ** 2 - 4 * nilai_a * nilai_c  # Menghitung diskriminan dengan rumus diskriminan

if nilai_a != 0:  # Nilai A tidak boleh 0
    if diskriminan < 0:  # Jika d < 0
        if nilai_a < 0:
            print("Fungsi f definit negatif")
        else:
            print("Fungsi f definit positif")
    elif diskriminan == 0:  # Jika d = 0
        print("Fungsi f memiliki 1 akar")
    else:  # Jika d > 0
        print("Fungsi f memiliki 2 akar")
else:  # Jika a = 0
    print("Nilai A tidak boleh 0")
