A = []
B = []

banyak_A = int(input('Berapa banyak elemen A yang ingin Anda masukkan? '))
for i in range(banyak_A):
    n_i = int(input('Masukkan elemen ke-' + str(i + 1) + ': '))
    A.append(n_i)
print('')

banyak_B = int(input('Berapa banyak elemen B yang ingin Anda masukkan? '))
for i in range(banyak_B):
    n_i = int(input('Masukkan elemen ke-' + str(i + 1) + ': '))
    B.append(n_i)
print('')

A_sorted = [A[i] for i in range(len(A))]
A_sorted.sort()

B_sorted = [B[i] for i in range(len(B))]
B_sorted.sort()

if A_sorted == B_sorted:
    print('B adalah anagram dari A\n')
else:
    print('B bukan anagram dari A\n')
