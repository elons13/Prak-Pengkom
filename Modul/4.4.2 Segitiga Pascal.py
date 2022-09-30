n = int(input('Masukkan N: '))

N = [[1 for j in range(n)] for i in range(n)]

for i in range(1, n):
    for j in range(1, n):
        N[i][j] = N[i - 1][j] + N[i][j - 1]

for i in range(n):
    for j in range(n):
        print(f'{N[i][j]:3}', end=' ')
    print('')