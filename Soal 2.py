nama = input("Masukkan nama anda: ")
nilai = int(input("Masukkan nilai anda: "))
if nilai >= 85:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah A")
elif nilai >= 84:
    print("Halo", nama,"Nilai anda setelah dikonversi adalah A-")
elif nilai >= 79:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah B+")
elif nilai >= 74:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah B")
elif nilai >= 69:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah C+")
elif nilai >= 64:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah C")
elif nilai <= 60:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah E")
else:
    print("Salah input")