class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tambah_stok(self, jumlah):
        self.stok += jumlah

    def kurangi_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False

class Toko:
    def __init__(self):
        self.inventaris = []

    def tambah_produk(self, produk):
        self.inventaris.append(produk)

    def hapus_produk(self, nama_produk):
        self.inventaris = [p for p in self.inventaris if p.nama != nama_produk]

    def tampilkan_produk(self):
        for produk in self.inventaris:
            print(f"Nama: {produk.nama}, Harga: {produk.harga}, Stok: {produk.stok}")

# Contoh penggunaan
toko = Toko()
produk1 = Produk("Laptop", 15000000, 10)
produk2 = Produk("Mouse", 150000, 50)

toko.tambah_produk(produk1)
toko.tambah_produk(produk2)

toko.tampilkan_produk()

# Menambah stok
produk1.tambah_stok(5)

# Mengurangi stok
if produk2.kurangi_stok(10):
    print("Stok berhasil dikurangi")
else:
    print("Stok tidak cukup")

toko.tampilkan_produk()
