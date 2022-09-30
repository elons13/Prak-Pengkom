from datetime import date as dt

tanggal = int(input('Masukkan tanggal lahir Anda: '))
bulan = int(input('Masukkan bulan lahir Anda: '))
tahun = int(input('Masukkan tahun lahir Anda: '))

hari_ini = dt.today()
tanggal_lahir = dt(tahun, bulan, tanggal)

umur_raw = hari_ini - tanggal_lahir
umur_tahun = int(umur_raw.days // 365)
umur_bulan_sisa = int((umur_raw.days % 365) // 30)


kamus_hari = {
    'Sunday': 'Minggu',
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu'
}

hari_lahir = f'{tanggal_lahir:%A}'

print(f'\nAnda lahir pada hari', kamus_hari[hari_lahir])
print(f'Umur Anda adalah {umur_tahun} tahun, {umur_bulan_sisa} bulan')
