def persegi():
    print('='*30)
    print('\tRUMUS PERSEGI')
    print('-'*30)

    s = int(input('MASUKAN SISI PERSEGI\t: '))

    L = lambda s: s * s
    K = lambda s: 4 * s

    print('LUAS PERSEGI\t\t:', L(s), "cm2")
    print('KELILING PERSEGI\t:', K(s), 'cm2')

persegi()