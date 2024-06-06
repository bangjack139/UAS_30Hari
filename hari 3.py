def penghitung_kata():
    kalimat = input("Masukkan sebuah kalimat: ")
    kata = kalimat.split()
    jumlah_kata = len(kata)
    
    print(f"Jumlah kata: {jumlah_kata}")

penghitung_kata()
