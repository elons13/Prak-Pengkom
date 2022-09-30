def kuadrat(A, B):
    for x in range(A, B + 1):
        hasil = x ** 2 - 2 * x + 5
        print('f(' + str(x) + ') = ' + str(hasil))


A = int(input('Masukkan A: '))
B = int(input('Masukkan B: '))

kuadrat(A, B)
