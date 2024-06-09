def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

def penghitung_faktorial():
    angka = int(input("Masukkan angka: "))
    hasil = faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")

penghitung_faktorial()
