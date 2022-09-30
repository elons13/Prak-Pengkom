# TUGAS PENDAHULUAN #1 PROBLEM 2

# KAMUS
# nim : int

# ALGORITMA
# Input NIM dari user
nim = int(input('Masukkan akhiran NIM: '))


# Percabangan untuk mencari kelas
if nim > 0 and nim % 2 == 0:  # Percabangan untuk NIM genap
    if 1 <= nim <= 100:  # NIM rentang 001-100
        print('Mahasiswa masuk ke kelas K2')
    elif 101 <= nim <= 200:  # NIM rentang 101-200
        print('Mahasiswa masuk ke kelas K4')
    elif 201 <= nim <= 300:  # NIM rentang 201-300
        print('Mahasiswa masuk ke kelas K6')
    elif nim > 300:  # NIM lebih dari 300
        print('Mahasiswa masuk ke kelas K8')
elif nim > 0:  # Percabangan untuk NIM ganjil
    if 1 <= nim <= 100:  # NIM rentang 001-100
        print('Mahasiswa masuk ke kelas K1')
    elif 101 <= nim <= 200:  # NIM rentang 101-200
        print('Mahasiswa masuk ke kelas K3')
    elif 201 <= nim <= 300:  # NIM rentang 201-300
        print('Mahasiswa masuk ke kelas K5')
    elif nim > 300:  # NIM lebih dari 300
        print('Mahasiswa masuk ke kelas K7')
else:
    print('NIM yang dimasukkan tidak valid')
