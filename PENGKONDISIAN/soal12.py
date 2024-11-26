nama = input('NAMA SISWA\t\t: ')
rentangnilai = int(input('NILAI SISWA (0-100)\t: '))

if rentangnilai >= 90:
    print('NILAI ADALAH A')
elif rentangnilai >= 80:
    print('NILAI ADALAH B')
elif rentangnilai >= 70:
    print('NILAI ADALAH C')
else:
    print('NILAI ADALAH E')