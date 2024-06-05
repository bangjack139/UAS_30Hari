def konversi_suhu():
    skala = input("Konversi ke (F)ahrenheit atau (C)elcius? ").upper()
    suhu = float(input("Masukkan suhu: "))

    if skala == 'F':
        hasil = (suhu * 9/5) + 32
    elif skala == 'C':
        hasil = (suhu - 32) * 5/9
    else:
        hasil = "Skala tidak valid"
    
    print(f"Hasil: {hasil}")

konversi_suhu()
