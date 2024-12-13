print("="*50)
print('\t TIGA BILANGAN BULAT (x, y, z)')
print("="*50)

x = int(input('Masukkan nilai x: '))
y = int(input('Masukkan nilai y: '))
z = int(input('Masukkan nilai z: '))

a = x
x = y
y = z
z = a
print(f'setelah dipertukarkan menjadi ({x}, {y}, {z})')