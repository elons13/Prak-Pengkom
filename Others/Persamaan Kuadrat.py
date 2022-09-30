import math
import cmath
import matplotlib.pyplot as plt
from numpy import linspace

print('''App ini bertujuan untuk menghitung solusi dari persamaan kuadrat dengan persamaan ax^2 + bx + c = 0
Anda akan diminta untuk memasukkan nilai a, b, dan c
Silahkan cek https://docs.python.org/3/library/math.html jika ingin memasukkan input yang lebih kompleks
''')


def solusi(a, b, c):
    # Menghitung diskriminan untuk persamaan
    diskriminan = b**2 - 4*a*c

    if diskriminan < 0:  # Mengecek apakah akarnya imajiner
        x1 = (-b + cmath.sqrt(diskriminan))/(2*a)
        x2 = (-b - cmath.sqrt(diskriminan))/(2*a)
        print(f'Akar tidak riil. x1 = {x1}, x2 = {x2}\n')

    else:
        x1 = (-b + math.sqrt(diskriminan))/(2*a)
        x2 = (-b - math.sqrt(diskriminan))/(2*a)
        if x1 == x2:
            if int(x1) == float(x1) and int(x2) == float(x2):
                print(f'Akar kembar. x1, x2 = {int(x1)}\n')
            else:
                print(f'Akar kembar. x1, x2 = {x1}\n')

        elif int(x1) == float(x1) and int(x2) == float(x2):
            print(f'x1 = {int(x1)}, x2 = {int(x2)}\n')

        else:
            print(f'x1 = {x1}, x2 = {x2}\n')


def Grafik(a, b, c):
    # Gatau, ini copas dari stackoverflow
    x = linspace(-10, 10, 1000)
    y = a*(x**2) + b*x + c
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


while True:
    try:  # Input dari user
        a = eval(input('Masukkan nilai a: '))
        b = eval(input('Masukkan nilai b: '))
        c = eval(input('Masukkan nilai c: '))
        solusi(a, b, c)

        # Grafik
        isGraph = input('Apakah ingin melihat grafik (Y/n)? ')
        print('\n')
        if isGraph.lower() == 'y':
            Grafik(a, b, c)  # Memunculkan grafik

    # Apabila input yang dimasukkan tidak sesuai dengan yang diinginkan
    except NameError:
        print('Tolong masukkan angka\n')
    except ZeroDivisionError:
        print('Nilai a tidak boleh 0\n')
    except:  # Untuk kesalahan lain yang tidak disebutkan di atas
        print('Ada yang salah dengan input yang dimasukkan, silahkan coba lagi\n')
