berat_badan = {
    "iza": 45,
    "opa": 50,
    "sadi": 66,
    "afi": 47,
    "fan": 55
    }

terberat = max(berat_badan, key=berat_badan.get)
print(f"Manusia terbesar berdasarkan berat adalah: {terberat} dengan berat {berat_badan[terberat]} kg.")
