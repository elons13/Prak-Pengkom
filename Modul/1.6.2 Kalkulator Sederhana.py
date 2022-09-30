n1 = int(input('Masukkan angka pertama: '))
n2 = int(input('Masukkan angka kedua: '))
operator = input('Masukkan operator: ')
print(f'{n1} {operator} {n2} = ', end='')

if operator == '+':
    hasil = n1 + n2
    print(hasil)
elif operator == '-':
    hasil = n1 - n2
    print(hasil)
elif operator == '/':
    hasil = n1 // n2
    print(hasil)
elif operator == '*':
    hasil = n1 % n2
    print(hasil)
elif operator == '%':
    hasil = n1 % n2
    print(hasil)
else:
    print('Operator yang diinput tidak valid\n')


