def bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def pengecek_bilangan_prima():
    angka = int(input("Masukkan angka: "))
    if bilangan_prima(angka):
        print(f"{angka} adalah bilangan prima")
    else:
        print(f"{angka} bukan bilangan prima")

pengecek_bilangan_prima()
