def prismasegitiga():
    print("="*40)
    print("\tRUMUS PRISMA SEGITIGA ")
    print("-"*40)

    S1 = int(input("MASUKAN SISI 1\t\t: "))
    S2 = int(input("MASUKAN SISI 2\t\t: "))
    S3 = int(input("MASUKAN SISI 3\t\t: "))
    a = int(input("MASULAN ALAS\t\t: "))
    t = int(input("MASUKAN TINGGI 1\t: "))
    t2 = int(input("MASUKAN TINGGI 2\t: "))

    ls = lambda S1,S2,S3,a,t,t2: (S1 + S2 + S3 ) * t2
    lp = lambda S1,S2,S3,a,t,t2: (S1 + S2 + S3 ) * t2 + a * t 
    vol = lambda S1,S2,S3,a,t,t2: 1/2 * a * t * t2 

    print("LUAS SELIMUT\t\t:",ls(S1,S2,S3,a,t,t2))
    print("LUAS PERMUKAAN\t\t:",lp(S1,S2,S3,a,t,t2))
    print("VOLUME\t\t\t:",vol(S1,S2,S3,a,t,t2))

prismasegitiga()