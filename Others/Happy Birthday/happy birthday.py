# File untuk ngasih ucapan selamat ulang tahun, bisa buat temen, sahabat, gebetan, ataupun dosen kalkulus lu
# Isinya bisa disesuaikan aja
# File satu lagi yang namanya "wishes.py" itu lebih baik ditaro di folder yang sama dan isinya juga disesuaikan aja

from time import sleep
from wishes import wishes
import random
from wishes import emoji
from datetime import date as dt


hari_ini = dt.today()
name = input('What would you like to be called? ').title()
input(f'Hello, {name}! Do you know what\'s special about today? ')
print(f'Yap! You are right. Today is {hari_ini:%A}')
sleep(3)
print('Just Kidding (￣y▽,￣)╭  \n\n')
sleep(2)


try:
    import pyfiglet
    wish = pyfiglet.figlet_format(f'\nHappy Birthday {name}', font='slant')
    print(wish)
except ModuleNotFoundError:
    print(f'Happy Birthday, {name}!\n\n')

sleep(1)
print('  *    *    *    *')
sleep(1)
print('  ||   ||   ||   ||')
sleep(1)
print('  ||   ||   ||   ||')
sleep(1)
print('=====================')
sleep(1)
print(f'Happy Birthday, {name}!')
sleep(1)
print('-----------------------')
sleep(1.5)
print('Good Luck on Your College!')
sleep(2)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n')
sleep(2)
print("Be happy!")
sleep(1.2)
print('Today is the day you were brought into this world to be a blessing and inspiration to the people around you!')
sleep(3.5)
print('You are a wonderful person!')
sleep(1.5)
print('May you be given more birthdays to fulfill all of your dreams!')
sleep(2)
print("from: Possibly the coolest and smartest guy you've ever met (～￣▽￣)～")
sleep(2)
input('\nDo you think it\'s cute? ')
print("You have to see this then")
sleep(1)
print('Are you ready?')
sleep(1)
print('3... (It will quite enough take your time to be end)')
sleep(2)
print('2... (Be patient)')
sleep(2)
print('1... (Bring it on!)')
sleep(2)

for i in range(1, 85):
    print('')

space = ' '
for i in range(1, 250):
    count = random.randint(1, 100)
    while count > 0:
        space += ' '
        count -= 1
    if i % 29 == 0:
        print(space + f'Happy Birthday, {name}(•̀ ω •́)✧!')
    elif i % 23 == 0:
        print(space + random.choice(wishes) + random.choice(emoji))
    elif i % 19 == 0:
        print(space + random.choice(wishes) + random.choice(emoji))
    elif i % 17 == 0:
        print('Happy Birthday' + random.choice(emoji))
    elif i % 13 == 0:
        print(space + random.choice(wishes) + random.choice(emoji))
    elif i % 11 == 0:
        print(space + random.choice(emoji))
    elif i % 7 == 0:
        print(space + random.choice(wishes) + random.choice(emoji))
    elif i % 5 == 0:
        print(space + random.choice(emoji))
    elif i % 3 == 0:
        print(space + random.choice(emoji))
    elif i % 2 == 0:
        print(space + random.choice(emoji))
    space = ' '
    sleep(0.5)

print(f"I took quotes from https://www.shutterfly.com/ideas/happy-birthday-quotes/ and made it appear randomly (emoji as well).")
