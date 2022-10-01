# Suatu program untuk mengubah gambar menjadi ascii
# Apa itu ascii? Coba aja ikutin
# Pertama, taro file gambar yang mau diubah di folder yang sama, ubah namanya jadi "gambar.png"
# Kalo gamau diubah atau formatnya bukan png juga gapapa, tapi nanti kode di baris 21 diganti jadi sesuai sama filenya
# Saran gua, buat run file ini make cmd/terminal, terus directorynya disesuaikan dengan directory folder ini
# Buat ganti directory di cmd, make command cd, kalo gak jelas coba cari di gugel
# Contoh, untuk kasus gua, gua naro folder ini di C:\Users\elonsquidion\OneDrive - Institut Teknologi Bandung\Tugas\Prak-Pengkom\Others\Ascii Image>
# Jadi, pas di cmd bakal baru jalan kalo directorynya sama
"""
Microsoft Windows [Version 10.0.22000.978]
(c) Microsoft Corporation. All rights reserved.

C:\Users\elonsquidion\OneDrive - Institut Teknologi Bandung\Tugas\Prak-Pengkom\Others\Ascii Image>
"""
# Kek gitu contohnya

import PIL.Image

img_flag = True

img = PIL.Image.open('gambar.jpg')

width, height = img.size
aspect_ratio = height / width
new_width = 145
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))

img = img.convert('L')

chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", ".", "#", "S", "?", ":"]

pixels = img.getdata()
new_pixels = [chars[pixel // 25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)
