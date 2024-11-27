umur = int(input("Masukkan umur Anda : "))
    
if umur < 12:
    tidur = 10
elif umur <= 18:
    tidur = 9
else:
    tidur = 8
    
print(f"Jumlah jam tidur yang disarankan: {tidur} jam per malam.")