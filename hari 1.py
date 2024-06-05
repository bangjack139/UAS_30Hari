def kalkulator():
    operasi = input("Masukkan operasi (tambah, kurang, kali, bagi): ").lower()
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if operasi == 'tambah':
        hasil = angka1 + angka2
    elif operasi == 'kurang':
        hasil = angka1 - angka2
    elif operasi == 'kali':
        hasil = angka1 * angka2
    elif operasi == 'bagi':
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Error: Pembagian dengan nol"
    else:
        hasil = "Operasi tidak valid"
    
    print(f"Hasil: {hasil}")

kalkulator()
