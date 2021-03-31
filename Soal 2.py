nama = input("Masukkan nama anda: ")
nilai = int(input("Masukkan nilai anda: "))
if nilai >= 85:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah A")
elif nilai >= 80:
    print("Halo", nama,"Nilai anda setelah dikonversi adalah A-")
elif nilai >= 75:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah B+")
elif nilai >= 70:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah B")
elif nilai >= 65:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah C+")
elif nilai >= 60:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah C")
elif nilai < 60:
    print("Halo", nama, "Nilai anda setelah dikonversi adalah E")
else:
    print("Salah input")