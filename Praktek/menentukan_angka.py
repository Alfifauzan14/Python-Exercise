angka = int(input("Masukan Angka : "))

if 100 <= angka <= 999:
    print("Ratusan")
elif 1000 <= angka <= 9999:
    print("Ribuan")
elif 1000000 <= angka <= 9999999:
    print("Jutaan")
else:
    print("error")