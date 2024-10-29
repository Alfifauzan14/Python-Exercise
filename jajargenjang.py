def jajargenjang():
    print("="*30)
    print("\tRUMUS JAJARGENJANG")
    print("-"*30)

    a = int(input('MASUKAN ALAS\t: '))
    t = int(input('MASUKAN TINGGIt\t: '))
    A = int(input('MASUKAN SISI A\t: '))
    B = int(input('MASUKAN SISI B\t: '))

    l = lambda a,t,A,B: a * t
    kel = lambda a,t,A,B: 2 * ( 1 + 2 )


    print('LUAS\t\t:',l(a,t,A,B))
    print('KELILING\t:',kel(a,t,A,B))

jajargenjang()