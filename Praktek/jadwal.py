jadwal = ()
    
for hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]:
    kegiatan = input(f"Masukkan kegiatan untuk hari {hari}: ")
    jadwal[hari] = kegiatan
    

print("\nJadwal Mingguan Anda:")

for hari, kegiatan in jadwal.items():
    print(f"{hari}: {kegiatan}")