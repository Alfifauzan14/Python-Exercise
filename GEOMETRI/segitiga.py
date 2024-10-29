def Segitiga():
    print('='*30)
    print('\tRUMUS SEGITIGA')
    print('-'*30)

    A = int(input("MASUKAN ALAS SEGITIGA\t: "))
    T = int(input("MASUKAN TINGGI SEGITIGA\t: "))
    s1 = int(input("MASUKAN SISI 1\t\t: "))
    s2 = int(input("MASUKAN SISI 2\t\t: "))
    s3 = int(input("MASUKAN SISI 3\t\t: "))

    L = lambda A,T,s1,s2,s3: 1/2 * A * T
    K = lambda A,T,s1,s2,s3: s1 + s2 + s3

    print("LUAS SEGITIGA\t\t:", L(A,T,s1,s2,s3), "Cm2")
    print("KELILING SEGITIGA\t:", K(A,T,s1,s2,s3), "Cm2")

Segitiga()