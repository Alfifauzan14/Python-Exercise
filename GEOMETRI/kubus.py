def kubus():
    print('='*30)
    print('\tRUMUS KUBUS')
    print('-'*30)

    s = int(input("MASUKAN SISI KUBUS\t: "))

    l = lambda s: 6 * s
    v = lambda s: s * 3

    print("LUAS KUBUS\t\t:", l(s), 'Cm2')
    print("VOLUME KUBUS\t\t:", v(s), 'Cm2')

kubus()