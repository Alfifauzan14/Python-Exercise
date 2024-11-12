jumlah = 0 
for h in range(2,12,2):
    if h < 10:
        print(h, end=' + ')
    else:
        print(h, end=' = ')
    jumlah = jumlah + (h)
print(jumlah)