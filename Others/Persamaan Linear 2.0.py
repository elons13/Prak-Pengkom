# Versi Kedua dari program persamaan linear
# Bisa menghitung persamaan linear dengan variabel yang banyak (mungkin dan semoga gak ada bug)

import numpy as np

banyak_variabel = int(input("Berapa banyak variabel persamaan yang ingin dicari: "))
print(f"Persamaan Linear {banyak_variabel} Variabel")
print(f"Akan ada {banyak_variabel} persamaan dan {banyak_variabel} variabel")
print("Anda akan diminta untuk memasukkan nilai tersebut satu demi satu\n")

koefisien = []
hasil = []

for i in range(banyak_variabel):
    print("Persamaan Ke-" + str(i + 1))
    for j in range(banyak_variabel):
        nilai = float(input(f"Masukkan koefisien variabel ke-" + str(j + 1) + ": "))
        koefisien.append(nilai)
        if j == banyak_variabel - 1:
            nilai = float(input(f"Masukkan hasil dari persamaan ke-" + str(i + 1) + ": "))
            hasil.append(nilai)
    print("\n")
            
koefisien = np.array(koefisien)
hasil = np.array(hasil)

koefisien = koefisien.reshape(banyak_variabel, banyak_variabel)
hasil = hasil.reshape(banyak_variabel, 1)
 
nilai_variabel = np.linalg.solve(koefisien, hasil)

for i in range(banyak_variabel):
    print(f"Nilai variabel ke-{str(i + 1)} adalah", end=" ")
    print(nilai_variabel[i][0])
