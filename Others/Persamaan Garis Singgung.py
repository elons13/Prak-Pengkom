import numpy as np

derajat = int(input("Berapa derajat polinomial yang ingin dicari? "))

polinomial = np.array([], dtype=float)
for i in range(derajat, -1, -1):
    k_i = int(input("Masukkan koefisien variabel berderajat ke-" + str(i) + ': '))
    polinomial = np.append(polinomial, k_i)
reversed_polinomial = np.flip(polinomial)

absis = int(input("Masukkan absis titik potong antara kurva dengan persamaan garis singgung: "))
pangkat = np.arange(derajat, -1, -1)

turunan = np.array([])
for i in range(derajat, 0, -1):
    k_i = i * reversed_polinomial[i]
    turunan = np.append(turunan, k_i)

reversed_turunan = np.flip(turunan)
pangkat_turunan = np.arange(derajat - 1, -1, -1)

y = np.sum(polinomial * np.power(absis, pangkat))
kemiringan = np.sum(turunan * np.power(absis, pangkat_turunan))


print('\nf(x)  = ', end='')
for i in range(derajat, 1, -1):
    print(str(reversed_polinomial[i]) + 'x^' + str(i), end=' + ')
print(str(reversed_polinomial[1]) + 'x + ' + str(reversed_polinomial[0]))

print('f\'(x) = ', end='')
for i in range(derajat - 1, 1, -1):
    print(str(reversed_turunan[i]) + 'x^' + str(i), end=' + ')
print(str(reversed_turunan[1]) + 'x + ' + str(reversed_turunan[0]))

print(f"Garis singgung di absis {absis} memiliki kemiringan {kemiringan}")
print(f"Persamaan Garis Singgung: y = {kemiringan}x + " + str((-1 * kemiringan * absis) + y))
