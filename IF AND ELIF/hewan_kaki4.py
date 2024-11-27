hewan_kaki_empat = ["Kucing", "Anjing", "Sapi", "Gajah"]

hewan_input = input("Masukkan nama hewan: ")

if hewan_input in hewan_kaki_empat:
    print(f"{hewan_input} memiliki empat kaki.")
else:
    print(f"{hewan_input} tidak memiliki empat kaki.")
