# TUGAS PENDAHULUAN #3 PROBLEM 3
# Deskripsi : Program untuk mengetahui apakah kedua kata bisa disambung dengan sub kata tertentu

# KAMUS
# banyak_1, banyak_2, i : int
# kata_1, kata_2 : str
# list_kata_1, list_kata_2, kata_sama : list
# dapat_disambung : bool

# ALGORITMA
# Input user
banyak_1 = int(input("Panjang kata pertama: "))
kata_1 = input("Kata pertama: ")
banyak_2 = int(input("Panjang kata kedua: "))
kata_2 = input("Kata kedua: ")

# Mengubah kata yang diinput user menjadi list
list_kata_1 = [huruf for huruf in kata_1]
list_kata_2 = [huruf for huruf in kata_2]

dapat_disambung = False  # Mengecek apakah bisa disambung atau tidak
i = 1  # Untuk indeks list
kata_sama = str(None)  # Untuk menampung semua huruf yang sama di kedua kata

# Mengecek apakah ada huruf yang sama
while i <= banyak_1 and i <= banyak_2:

    # Membagi-bagi array of character menjadi beberapa sub kata
    sub_kata_1 = [list_kata_1[j] for j in range(banyak_1-i, banyak_1)]  # Dimulai dari belakang sebanyak i elemen
    sub_kata_2 = [list_kata_2[j] for j in range(i)]  # Dimulai dari depan sebanyak i elemen
    
    if sub_kata_1 == sub_kata_2:  # Apabila ada yang sama, masukkan sub kata tersebut ke dalam kata_sama
        dapat_disambung = True
        kata_sama = sub_kata_1
    
    i += 1  # Mengincrement i

# Output
if dapat_disambung:
    print("Kedua kata dapat disambung dengan sub kata '", end='')
    for huruf in kata_sama:
        print(huruf, end='')
    print("'.")
    
else:  # Jika tidak ada sub kata yang sama
    print("Kedua kata tidak dapat disambung.")
