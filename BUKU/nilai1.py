print("="*40)
print("\tMENENTUKAN NILAI MAHASISWA")
print("="*40)

rentangnilai = int(input('NILAI MAHASISWA (0-100)\t: '))

if rentangnilai >= 80:
    print('NILAI ADALAH A')
elif rentangnilai >= 70:
    print('NILAI ADALAH B')
elif rentangnilai >= 55:
    print('NILAI ADALAH C')
elif rentangnilai >= 40:
    print('NILAI ADALAH D')
else:
    print('NILAI ADALAH E')