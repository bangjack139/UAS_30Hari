import random

def generator_angka_acak():
    try:
        batas_bawah = int(input("Masukkan batas bawah: "))
        batas_atas = int(input("Masukkan batas atas: "))

        if batas_bawah > batas_atas:
            print("Batas bawah tidak boleh lebih besar dari batas atas.")
            return

        angka_acak = random.randint(batas_bawah, batas_atas)
        print(f"Angka acak: {angka_acak}")
    except ValueError:
        print("Harap masukkan nilai numerik yang valid.")

generator_angka_acak()
