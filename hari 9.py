def pembalik_kata():
    kalimat = input("Masukkan sebuah kalimat: ")
    kata = kalimat.split()
    kata_balik = kata[::-1]
    
    kalimat_balik = ' '.join(kata_balik)
    print(f"Kalimat terbalik: {kalimat_balik}")

pembalik_kata()
