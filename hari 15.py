class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Keranjang:
    def __init__(self):
        self.produk_list = []

    def tambah_produk(self, produk):
        self.produk_list.append(produk)

    def hapus_produk(self, produk):
        self.produk_list.remove(produk)

    def total_harga(self):
        return sum(produk.harga for produk in self.produk_list)  # Memperbaiki syntax list comprehension

class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.keranjang = Keranjang()

    def lihat_keranjang(self):
        for produk in self.keranjang.produk_list:
            print(f"Nama: {produk.nama}, Harga: {produk.harga}")

    def checkout(self):
        total = self.keranjang.total_harga()
        print(f"Total harga: {total}")
        self.keranjang = Keranjang()  # Mengosongkan keranjang setelah checkout

# Contoh penggunaan
produk1 = Produk("lcd", 13000000)
produk2 = Produk("Mouse", 150000)

pelanggan = Pelanggan("John Doe")

# Menambahkan produk ke keranjang
pelanggan.keranjang.tambah_produk(produk1)
pelanggan.keranjang.tambah_produk(produk2)

# Melihat isi keranjang
pelanggan.lihat_keranjang()

# Melakukan checkout
pelanggan.checkout()
