# TUGAS PENDAHULUAN #1 PROBLEM 3

# KAMUS
# jam_mulai : int
# menit_mulai : int
# detik_mulai : int
# jam_selesai : int
# menit_selesai : int
# detik_selesai : int
# lama_jam : int
# lama_menit : int
# lama_detik : int

# ALGORITMA
# Input user untuk waktu dimulai lari dan selesai lari
print('Masukkan waktu mulai!')
jam_mulai = int(input('Jam    :  '))
menit_mulai = int(input('Menit  :  '))
detik_mulai = int(input('Detik  :  '))
print('Masukkan waktu selesai!')
jam_selesai = int(input('Jam    :  '))
menit_selesai = int(input('Menit  :  '))
detik_selesai = int(input('Detik  :  '))


# Menghitung lama jam bisa dilakukan dengan mengurangkan jam selesai dengan jam mulai
lama_jam = jam_selesai - jam_mulai

# Menghitung lama menit, bisa dilakukan percabangan
if (menit_selesai - menit_mulai) < 0:
    lama_jam -= 1  # 1 jam diubah menjadi menit
    lama_menit = (menit_selesai + 60) - menit_mulai  # 60 didapatkan dari konversi 1 jam ke menit yaitu 60 menit
else:
    lama_menit = menit_selesai - menit_mulai

# Menghitung lama detik, bisa dilakukan percabangan
if (detik_selesai - detik_mulai) < 0:
    lama_menit -= 1  # 1 menit diubah menjadi detik
    lama_detik = (detik_selesai + 60) - detik_mulai  # 60 didapatkan dari konversi 1 menit ke detik yaitu 60 detik
else:
    lama_detik = detik_selesai - detik_mulai


# Output lama lari
if lama_jam == 0 and lama_menit == 0:
    print(f'Tuan Riz berlari selama {lama_detik} detik')  # Hanya ditampilkan detik saja
elif lama_jam == 0:
    print(f'Tuan Riz berlari selama {lama_menit} menit {lama_detik} detik')  # Hanya ditampilkan menit dan detik
else:
    print(f'Tuan Riz berlari selama {lama_jam} jam {lama_menit} menit {lama_detik} detik')
