# PRAKTIKUM #1 PROBLEM 1

# KAMUS
# nilai_uts : float
# nilai_pr : float
# nilai_tubes : float
# nilai_akhir_tanpa_uas : float
# nilai_uas_min : float

# ALGORITMA
# Input nilai UTS, PR, dan Tubes
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_pr = float(input("Masukkan nilai PR: "))
nilai_tubes = float(input("Masukkan nilai Tubes: "))

nilai_akhir_tanpa_uas = nilai_uts * 0.35 + nilai_pr * 0.1 + nilai_tubes * 0.2  # Menghitung nilai akhir sementara tanpa nilai UAS
nilai_uas_min = (75 - nilai_akhir_tanpa_uas) / 0.35  # Nilai UAS minimum didapatkan dari selisih nilai yang diperlukan dibagi dengan 35%

if nilai_uas_min > 100:  # Nilai UAS tidak mungkin melebihi 100
    print("Tuan Leo tidak akan mungkin mendapatkan indeks A")
else:  # Output nilai UAS minimum
    print(f"nilai UAS minimum yang diperlukan adalah {nilai_uas_min:.2f}") 
