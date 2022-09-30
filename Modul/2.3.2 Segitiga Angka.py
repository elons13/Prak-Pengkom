n = int(input('Masukkan bilangan positif: '))
segitiga = ""
if n > 0:
    for i in range(1, n + 1):
        segitiga += str(i) + " "
        print(segitiga)
else:
    print('Tolong masukkan bilangan positif yang valid')
