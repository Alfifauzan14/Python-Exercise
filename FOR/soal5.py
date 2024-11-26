jumlah = 0 
for e in range(1, 6):
    if e < 5:
        print(e, end=' + ')
    else:
        print(e, end=' = ')
    jumlah = jumlah + (e)
print(jumlah)