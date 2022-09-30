panjang = int(input("Masukkan panjang string: "))
kata = str(input('Masukkan string: ')).lower()

list_huruf = [i for i in kata]

list_huruf_belakang = [list_huruf[i] for i in range(panjang - 1, -1, -1)]

if list_huruf == list_huruf_belakang:
    print(f'{kata} merupakan palindrom')
else:
    print(f'{kata} bukan merupakan palindrom')
