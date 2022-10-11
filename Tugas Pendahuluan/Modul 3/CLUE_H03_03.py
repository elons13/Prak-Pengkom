# Problem tersulit untuk TP Modul 3, perlu bener-bener bisa dan tahu apa yang terjadi pada problem sebelumnya supaya bisa mengerjakan problem ini

# Idenya adalah, secara bersamaan, kita mengecek kata pertama dari belakang dan mengecek kata kedua dari depan
# Apabila ada yang sama, maka kata bisa disambung
# Misal
ukuran_pertama = 8
kata_pertama = "institut" 
ukuran_kedua = 5
kata_kedua = "utara"
# Kita akan mulai dari 1 huruf terakhir pada kata_pertama (t) dan huruf awal dari kata_pertama (u)
# Masih, tidak sama, maka akan kita tingkatkan ke pengecekan 2 huruf
# 2 huruf terakhir pada kata_pertama (ut) dan huruf awal dari kata_pertama (ut)
# Sama, maka bisa disambung
# Apabila sampai akhir ada yang sama maka tidak bisa disambung

# Pertama, ubah kedua kata menjadi list supaya mudah dicek, misal dengan list comprehension
list_kata_pertama = [huruf for huruf in kata_pertama]
list_kata_kedua = [huruf for huruf in kata_kedua]

# Lalu, bagaimana jika ingin mengecek sebanyak angka tertentu pada list?
# Cara yang gua tawarkan adalah seperti ini
# Template ketika ini memanggil indeks tertentu pada suatu list adalah list_kata_pertama[awal:akhir:step]
# Jika awalnya tidak diisi, akan dianggap dari awal, misal
print(list_kata_pertama[:2:1])
# Kode tersebut akan mengeprint indeks 0 hingga 1, 2 tidak termasuk
# Jika akhirnya tidak diisi, akan dianggap sampai akhir, misal
print(list_kata_pertama[1::1])
# Kode tersebut akan mengeprint indeks 1 hingga selesai
# Step adalah, berapa beda dari satu indeks ke indeks berikutnya, misal
print(list_kata_pertama[::2])
# Kode tersebut akan mengeprint indeks 0, 2, 4, dan 6. Jika tidak diisi maka defaultnya adalah 1

# Lalu, contoh penggunaannya untuk problem ini adalah seperti berikut
for i in range(5):
    sub_kata_pertama = list_kata_pertama[ukuran_pertama-1-i:ukuran_pertama]  # Membuat list baru yang isi anggotanya, pada kasus ini, dimulai dari list_ukuran_pertama indeks 7-i hingga 8
    sub_kata_kedua = list_kata_kedua[0:i+1]  # # Membuat list baru yang isi anggotanya, pada kasus ini, dimulai dari list_ukuran_kedua indeks 0 hingga i+1
    if sub_kata_pertama == sub_kata_kedua:
        print(sub_kata_pertama)
# Kode di atas meskipun jalan tetapi hanyalah contoh biar lu kebayang mau diapain dengan informasi yang gua kasih tau mengenai [:::]
# Harus ada beberapa (bahkan hampir semua) yang perlu diganti biar program ini jalan dengan apapun kemungkinan user
# Seperti biasa, algoritmanya boleh ngikutin, nggak itu lebih baik biar menguji kreativitas
# Syntax, Output, dan keberjalanan kode gua serahin ke elu
