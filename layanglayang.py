def layang_layang():
    print('='*40)
    print('\tRUMUS LAYANG LAYANG')
    print('-'*40)

    diagonal1 = int(input("MASUKAN DIAGONAL 1\t\t: "))
    diagonal2 = int(input("MASUKAN DIAGONAL 2\t\t: "))
    a = int(input("MASUKAN SISI A\t\t\t: "))
    b = int(input("MASUKAN SISI B\t\t\t: "))

    L = lambda diagonal1,diagonal2,a,b: diagonal1 * diagonal2
    K = lambda diagonal1,diagonal2,a,b: 2 * ( a + b )

    print("LUAS LAYANG LAYANG\t\t:", L(diagonal1,diagonal2,a,b), 'Cm2')
    print("KELILING LAYANG LAYANG\t\t:", K(diagonal1,diagonal2,a,b), 'Cm2')

layang_layang()