# Sesuai dengan asumsi yang gua pakai untuk array statis (baca clue 01), pada clue ini akan gua kasih tau gimana caranya bikin array statis
# Artinya, kita akan inisisasi list dengan ukuran tertentu dan akan dipastikan tidak akan berubah
# Misal, ukuran list yang akan kita miliki adalah 4
ukuran = 4
# Idenya adalah kita menerima input dari user (dalam kasus ini ada 4) lalu kita tampung dalam list
# Kemudian, nilai dari list tersebut akan kita cek kesamaan antara satu dengan yang lainnya

# Pertama, kita akan buat list kosong yang berukuran 4, ada 2 cara yang gua tawarkan

# 1
list_bilangan = [None] * ukuran

# 2, list comprehension
list_bilangan = [None for i in range(ukuran)]
# Maksudnya, ketika i = 0, kita masukkan None ke dalam list, begitu terus hingga i = 3 sehingga ada None sebanyak 4 kali

# Kita ingin mengganti nilai pada list_bilangan yang awalnya None semua dengan input dari user tersebut
# Tentunya kita melakukan hal tersebut menggunakan for loop

for i in range(ukuran):
    bilangan = int(input())
    list_bilangan[i] = bilangan

# Yang terjadi adalah, ketika i = 0, kita meminta input dari user, lalu input tersebut akan menjadi indeks ke-0 pada list_bilangan

# Berikutnya adalah mengecek nilai satu sama lain, dan sebenarnya cukup simpel
# Indeks ke-0, akan dicek dengan indeks ke-1,2,3
# Indeks ke-1, akan dicek dengan indeks ke-0,2,3
# dst.

# Cara yang paling elegan (mungkin) untuk melakukannya adalah dengan double for loop lagi
# Loop pertama untuk indeks yang ingin dicek
# Loop kedua untuk indeks yang dengan apa diceknya
# Dengan syarat bahwa indeks pada loop pertama tidak sama dengan indeks pada loop kedua
# Semoga bisa dimengerti, penulisan syntaxnya (termasuk outputnya dan bagaimana bisa berjalan) gua serahkan kepada lu
