# Membuat fungsi untuk mengetahui jenis dari bilangan positif apakah ganjil/genap
N = int(input("Masukkan nilai N: "))

if N > 0:
    if N % 2 == 0:
        print(f'{N} bilangan positif genap\n')
    else:
        print(f'{N} bilangan positif ganjil\n')
else:
    print('Silahkan masukkan bilangan positif yang valid\n')
