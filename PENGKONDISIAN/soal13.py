x = int(input('MASUKAN NILAI X\t: '))
y = int(input('MASUKAN NILAI Y\t: '))
z = int(input('MASUKAN NILAI Z\t: '))

if x >= y and x >= z:
    terbesar = x
elif y >= x and y >= z:
    terbesar = y
else:
    terbesar = z

if x <=y and x <= z:
    terkecil = x
elif y <= x and y <= z:
    terkecil = y
else:
    terkecil = z

print('NILAI TERBESAR\t:', terbesar)
print('NILAI TERKECIL\t:', terkecil)