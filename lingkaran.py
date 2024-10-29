def lingkaran():
    print('='*30)
    print('\tRUMUS LINGKARAN')
    print('-'*30)

    PHI = 3.14
    r = int(input('MASUKAN JARI JARI\t: '))

    l = lambda r: PHI * r * r
    k = lambda r: PHI * 2 * r

    print('LUAS LINGKARAN\t\t:',l(r))
    print('KELILING LINGKARAN\t:',k(r))

lingkaran()