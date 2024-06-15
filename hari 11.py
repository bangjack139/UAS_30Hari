class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status = "Tersedia"

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            return True
        return False

    def kembali(self):
        self.status = "Tersedia"

class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_pinjam = None

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_pinjam = buku
            return True
        return False

    def kembalikan_buku(self):
        if self.buku_pinjam:
            self.buku_pinjam.kembali()
            self.buku_pinjam = None

class Perpustakaan:
    def __init__(self):
        self.buku_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)

    def cari_buku(self, judul):
        for buku in self.buku_list:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

# Contoh penggunaan
perpus = Perpustakaan()
buku1 = Buku("Python 101", "Guido")
buku2 = Buku("Learn C++", "Bjarne")

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

anggota = Anggota("John Doe")

# Meminjam buku
buku_dicari = perpus.cari_buku("Python 101")
if buku_dicari and anggota.pinjam_buku(buku_dicari):
    print(f"{anggota.nama} berhasil meminjam buku '{buku_dicari.judul}'")
else:
    print("Buku tidak tersedia atau sudah dipinjam")

# Mengembalikan buku
anggota.kembalikan_buku()
print(f"{anggota.nama} telah mengembalikan buku")

# Memeriksa status buku setelah dikembalikan
if buku_dicari:
    print(f"Status buku '{buku_dicari.judul}': {buku_dicari.status}")
