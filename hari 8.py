def pengurut_angka():
    angka = input("Masukkan daftar angka (pisahkan dengan koma): ")
    angka_list = [int(x) for x in angka.split(',')]
    
    angka_list.sort()
    print(f"Daftar angka terurut: {angka_list}")

pengurut_angka()
