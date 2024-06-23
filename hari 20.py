class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Pesanan:
    def __init__(self):
        self.items = []

    def tambah_item(self, menu):
        self.items.append(menu)

    def hapus_item(self, menu):
        self.items.remove(menu)

    def total_harga(self):
        return sum(item.harga for item in self.items)

class Restoran:
    def __init__(self):
        self.menu_list = []
        self.pesanan_list = []

    def tambah_menu(self, menu):
        self.menu_list.append(menu)

    def buat_pesanan(self):
        pesanan = Pesanan()
        self.pesanan_list.append(pesanan)
        return pesanan

    def tampilkan_menu(self):
        for menu in self.menu_list:
            print(f"Nama: {menu.nama}, Harga: {menu.harga}")

# Contoh penggunaan
restoran = Restoran()
menu1 = Menu("Nasi Goreng", 25000)
menu2 = Menu("Mie Goreng", 20000)

restoran.tambah_menu(menu1)
restoran.tambah_menu(menu2)

# Tampilkan menu
restoran.tampilkan_menu()

# Buat pesanan
pesanan = restoran.buat_pesanan()
pesanan.tambah_item(menu1)
pesanan.tambah_item(menu2)

# Tampilkan total harga pesanan
print(f"Total harga: {pesanan.total_harga()}")
