jad_makan = ["Sarapan", "Makan Siang", "Makan Malam"]
menu = []
for makan in jad_makan:
    menu_item = input(f"Masukkan menu untuk {makan}: ")
    menu.append(menu_item)
print("Jadwal makan hari ini:", dict(zip(jad_makan, menu)))
