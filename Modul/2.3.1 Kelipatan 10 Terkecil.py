n_raw = input("Masukkan N: ")
n = int(n_raw)

if n > 0:
    print(1, end='')
    for i in range(len(n_raw)):
        print(0, end='')
else:
    print("Input tidak valid")