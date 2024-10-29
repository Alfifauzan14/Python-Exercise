def kerucut():
    print("="*30)
    print("\tRUMUS KERUCUT")
    print("-"*30)

    PHI = 3.14
    r = int(input('MASUKAN JARI-JARI\t: '))
    s = int(input('MASUKAN SISI\t\t: '))
    t = int(input('MASUKAN TINGGI\t\t: '))

    ls = lambda r,s,t: PHI * r * s
    lp = lambda r,s,t: ( PHI * r * s ) + ( PHI * r ** 2 )
    v = lambda r,s,t: 1/3 * PHI * r ** 2 * t

    print('LUAS KERUCUT\t\t:',ls(r,s,t))
    print('LUAS PERMUKAAN\t\t:',lp(r,s,t))
    print('VOLUME\t\t\t:',v(r,s,t))

kerucut()