# TUGAS PENDAHULUAN #1 PROBLEM 1

# KAMUS
# harga_dasar_A : int
# harga_jual_A : int
# harga_dasar_B : int
# harga_jual_B : int
# harga_dasar_C : int
# harga_dasar_C : int
# keuntungan_A : int
# keuntungan_B : int
# keuntungan_C : int

# ALGORITMA
# Input dari user untuk harga dasar dan harga jual dari ketiga barang
harga_dasar_A = int(input('Masukkan harga dasar barang A: '))
harga_jual_A = int(input('Masukkan harga jual barang A: '))

harga_dasar_B = int(input('Masukkan harga dasar barang B: '))
harga_jual_B = int(input('Masukkan harga jual barang B: '))

harga_dasar_C = int(input('Masukkan harga dasar barang C: '))
harga_jual_C = int(input('Masukkan harga jual barang C: '))


# Menentukan keuntungan masing-masing barang
keuntungan_A = harga_jual_A - harga_dasar_A
keuntungan_B = harga_jual_B - harga_dasar_B
keuntungan_C = harga_jual_C - harga_dasar_C


# Membuat percabangan untuk menentukan barang yang harus ditawarkan
if keuntungan_A > keuntungan_B and keuntungan_A > keuntungan_C:  # Barang A memiliki keuntungan tertinggi
    print('Barang yang harus ditawarkan adalah barang A')
elif keuntungan_B > keuntungan_C and keuntungan_B > keuntungan_A:  # Barang B memiliki keuntungan tertinggi
    print('Barang yang harus ditawarkan adalah barang B')
elif keuntungan_C > keuntungan_A and keuntungan_C > keuntungan_B:  # Barang C memiliki keuntungan tertinggi
    print('Barang yang harus ditawarkan adalah barang C')
else:  # Selain tiga kondisi di atas
    print('Ada barang yang memiliki keuntungan yang sama')
