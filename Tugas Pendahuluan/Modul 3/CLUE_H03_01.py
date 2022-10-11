# Idenya adalah kita ingin membalik kata yang diinput oleh user, lalu diprint mulai dari belakang
# Katakanlah
kata = "abcd"
# kita balik menjadi dcba, lalu kita print mulai dari awal menjadi
# a 
# ba 
# cba 
# dcba 
# salah satu cara untuk melakukannya adalah dengan mengubah kata yang awalnya string menjadi list supaya bisa dibalik
# ada 2 cara yang gua tawarkan

# 1
list_kata = []
for huruf in kata:
    list_kata += huruf

# 2
# Cara ini merupakan penyingkatan dari cara pertama, disebut list comprehension
list_kata = [huruf for huruf in kata]
# Cara ini juga merupakan cara yang gua sarankan
# Di bitly BanListPengkom, dikatakan bahwa array yang kita buat adalah array statis sehingga operasi dinamis tidak diperbolehkan
# Gua mengasumsikan maksud dari array statis adalah ukuran dari array tersebut tidak boleh pertama
# Pada cara 1, ukuran arraynya gua deklarasi dengan ukuran 0 (tidak ada isinya), lalu ukurannya berubah menjadi 4, yaitu ['a', 'b', 'c', 'd']
# Ukurannya berubah, sehingga array tersebut merupakan array yang dinamis, jadi cara ini yang gua sarankan

# Berikutnya yang akan kita lakukan adalah membalik nilai list pada list_kata
# Untuk ini gua serahkan ke diri kalian, pada folder "Modul" ada file "3.2.1 Reverse.py" yang bisa dijadiin referensi
# Bisa juga lu cari-cari di internet atau mungkin mau mencoba sendiri untuk latihan

# Setelahnya kita mau mengeprint nilai pada list mulai dari belakang
# Ada 1 cara yang gua tawarkan
# Ketika ingin mengeprint nilai list pada variabel tertentu, kita bisa menggunakan kurung siku, misal

print(list_kata[0])
# Outputnya adalah 'a' karena indeks ke-0 pada list_kata adalah a
# Ingat, indeks dimulai dari 0

# Hal tersebut bisa kita gabung dengan for loop, misal
for i in range(2):
    print(list_kata[i])

# Outputnya adalah
'''
a
b
'''
# For loop akan mengeprint mulai dari indeks 0 hingga 1, 2 tidak termasuk
# Dalam kondisi default, ketika kita mengeprint sesuatu akan diakhiri dengan garis baru sehingga print setelahnya berada pada baris yang baru
# Kita bisa mengubah nilainya dengan parameter end pada print
for i in range(2):
    print(list_kata[i], end='')
# Sekarang, outputnya sudah dalam satu baris
# ab

# Supaya bisa mengeprint satu-satu, cara yang gua tawarkan adalah dengan double for loop
# loop pertama berguna untuk mengeprint mulai dari mana
for i in range(1, 5):
    # Loop kedua berguna untuk mengeprint sampai mana
    for j in range(i):
        print(list_kata[j], end='')
    print('')  # Ini berguna untuk membuat garis baru apabila iterasi kedua telah selesai

# Outputnya adalah
'''
a
ab
abc
abcd
'''
# Sesuai dengan apa yang diinginkan

# Biar gua jelasin apa yang terjadi pada kedua loop tersebut, pada
# for i in range(1, 5)
# Telah kita ketahui, pertama i = 1, kemudian i = 2, dst. sampai i = 4 (5 tidak termasuk)
# pada
    # for j in range(i):
# Pada saat i = 1, maka j = 0, maka akan mengeprint indeks ke-0
# Pada saat i = 2, maka j = 0, kemudian j = 1, akan mengeprint indeks ke-0, 1
# dst. sampai i = 5

# Yup, itu jika kita print satu-satu dari depan, jika diprint satu-satu dari belakang gua serahin ke kalian, cuma ganti rangenya aja kok, cuma perlu kreatif aja
# Algoritmanya bisa ngikutin, tapi kalau mau ada yang diubah itu lebih baik biar menambah kreativitas