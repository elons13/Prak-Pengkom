from random import randint

print('''Selamat datang di permainan Tebak Angka
Pada game ini, Anda akan diminta untuk menebak suatu angka tersembunyi antara rentang 1-1000
Anda hanya memiliki 15 kesempatan untuk menebak angka tersebut sebelum akhirnya game over''')

apakah_main = True
while apakah_main:
    skor = 15
    angka_kunci = randint(1,1000)
    while skor >= 0:
        try:
            angka_tebak = False
            if skor > 0 and angka_tebak != angka_kunci:
                angka_tebak = int(input('Masukkan angka tebakkan Anda: '))
                if angka_tebak > angka_kunci:
                    skor -= 1
                    print('Angka tebakkan salah, terlalu besar. Silahkan tebak lagi!\n')
                elif angka_tebak < angka_kunci:
                    skor -= 1
                    print('Angka tebakkan salah, terlalu kecil. Silahkan tebak lagi!\n')
                else:
                    print(f'Selamat, angka tebakkan benar. Skor Anda adalah {skor}/15\n')
                    break
            else:
                print('Permainan selesai. Anda gagal menebak angka tersembunyi')
                break
        except:
            print('Masukkan angka yang valid\n')

    apakah_main_mentah = input('Apakah mau main lagi? (Y/n): ').lower()
    if apakah_main_mentah != 'y':
        apakah_main = False

print('Terima kasih sudah bermain. Sampai jumpa!')