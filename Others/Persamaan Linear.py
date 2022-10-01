import numpy as np

print('Kalkulator ini digunakan untuk menjawab persamaan linear 2 dan 3 variabel.')
print('Ketik "2" untuk menjawab Persamaan Linear Dua Variabel')
print('Ketik "3" untuk menjawab Persamaan Linear Tiga Variabel')

while True:
    jenis = int(input("Masukkan pilihan Anda: "))
    if jenis == 2 or jenis == 3:
        break
    else:
        print("Masukkan pilihan jawaban yang valid!")

# Untuk menjawab Persamaan Linear Dua Variabel
if jenis == 2:
    print("""Persamaan Linear Dua Variabel memiliki persamaan umum
    a1x + b1y = k1
    a2x + b2y = k2
    """)
    a1 = float(input("Masukkan nilai a1: "))
    b1 = float(input("Masukkan nilai b1: "))
    k1 = float(input("Masukkan nilai k1: "))
    a2 = float(input("Masukkan nilai a2: "))
    b2 = float(input("Masukkan nilai b2: "))
    k2 = float(input("Masukkan nilai k2: "))

    pers = np.array([[a1, b1], [a2, b2]])
    hasil = np.array([[k1], [k2]])
else:
    print("""Persamaan Linear Tiga Variabel memiliki persamaan umum
    a1x + b1y + c1z = k1
    a2x + b2y + c2z = k2
    a3x + b3y + c3z = k3
    """)
    a1 = float(input("Masukkan nilai a1: "))
    b1 = float(input("Masukkan nilai b1: "))
    c1 = float(input("Masukkan nilai c1: "))
    k1 = float(input("Masukkan nilai k1: "))
    a2 = float(input("Masukkan nilai a2: "))
    b2 = float(input("Masukkan nilai b2: "))
    c2 = float(input("Masukkan nilai c2: "))
    k2 = float(input("Masukkan nilai k2: "))    
    a3 = float(input("Masukkan nilai a3: "))
    b3 = float(input("Masukkan nilai b3: "))
    c3 = float(input("Masukkan nilai c3: "))
    k3 = float(input("Masukkan nilai k3: "))

    pers = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    hasil = np.array([[k1], [k2], [k3]])

try:
    perhitungan = np.linalg.solve(pers, hasil)
except:
    print("Tidak ada solusi")

if jenis == 2:
    x = perhitungan[0][0]
    y = perhitungan[1][0]
    print(f"x = {x}, y = {y}")
else:
    x = perhitungan[0][0]
    y = perhitungan[1][0]
    z = perhitungan[2][0]
    print(f"x = {x}, y = {y}, z = {z}")
