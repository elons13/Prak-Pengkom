# TUGAS PENDAHULUAN #3 PROBLEM 1
# Deskripsi : Program untuk mencetak suatu kata yang diinput user secara terbalik

# KAMUS
# panjang : int
# kata : str
# list_huruf : list
# list_huruf_terbalik : list

# ALGORITMA
# Input user
panjang = int(input("Masukkan N: "))
kata = input("Masukkan kata: ")

# Mengubah string ke list
list_huruf = [huruf for huruf in kata]
list_huruf_terbalik = [list_huruf[i] for i in range(panjang-1, -1, -1)]  # Membalik list dengan mengulang dari akhir ke awal

#  Iterasi untuk mencetak nilai list_huruf_terbalik mulai dari belakang
for i in range(panjang-1, -1, -1):
    for j in range(i, panjang):
        print(list_huruf_terbalik[j], end='')
    print('')  # Melakukan 'new line' setelah mencetak satu iterasi
