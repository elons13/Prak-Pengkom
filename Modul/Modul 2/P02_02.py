# PRAKTIKUM #2 PROBLEM 2
# Deskripsi : Program untuk mengetahui bilangan prima dari bilangan random

# KAMUS
# is_prima : bool
# prima, bisa_dibagi : int

# ALGORITMA
is_prima = False
prima = 0
bisa_dibagi = 0

while not is_prima:
    bilangan = int(input("Masukkan bilangan untuk diperiksa: "))
    if bilangan >= 2:
        for j in range(2, bilangan):
            if bilangan % j == 0:
                bisa_dibagi += 1
        if bisa_dibagi == 0:
            is_prima = True
        bisa_dibagi = 0

print(f"Bilangan {bilangan} adalah bilangan prima!")