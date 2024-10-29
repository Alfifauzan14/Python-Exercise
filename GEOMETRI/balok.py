def balok():
    print('='*30)
    print('\tRUMUS BALOK')
    print('-'*30)

    p = int(input("MASUKAN PANJANG\t: "))
    l = int(input("MASUKAN LEBAR\t: "))
    t = int(input("MASUKAN TINGGI\t: "))

    v = lambda p,l,t: p * l * t

    print("VOLUME BALOK\t:", v(p,l,t), "Cm3")

balok()