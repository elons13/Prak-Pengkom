banyak = int(input('Masukkan N: '))
x = []
for i in range(banyak):
    n_i = input()
    x += n_i
print('Hasil dibalik:')
for i in range(banyak - 1, -1, -1):
    print(x[i], end=' ')
