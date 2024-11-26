total_harga = int(input('MASUKAN HARGA BARANG\t:Rp. '))

if total_harga >= 100000:
    diskon = total_harga*0.05 # diskon 5%

total_bayar = total_harga-diskon

print('DISKON\t\t\t:Rp.' ,diskon)
print('TOTAL YANG DI BAYAR\t:Rp.' ,total_bayar )