class Kamar:
    def __init__(self, nomor, tipe):
        self.nomor = nomor
        self.tipe = tipe
        self.tersedia = True

    def pesan(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def batalkan_pesan(self):
        self.tersedia = True

class Pelanggan:
    def __init__(self, nama):
        self.nama = nama

class Reservasi:
    def __init__(self, pelanggan, kamar):
        self.pelanggan = pelanggan
        self.kamar = kamar

class Hotel:
    def __init__(self):
        self.kamar_list = []

    def tambah_kamar(self, kamar):
        self.kamar_list.append(kamar)

    def cari_kamar(self, nomor):
        for kamar in self.kamar_list:
            if kamar.nomor == nomor:
                return kamar
        return None

    def buat_reservasi(self, pelanggan, nomor_kamar):
        kamar = self.cari_kamar(nomor_kamar)
        if kamar and kamar.pesan():
            return Reservasi(pelanggan, kamar)
        return None

# Contoh penggunaan
hotel = Hotel()
kamar1 = Kamar(101, "Single")
kamar2 = Kamar(102, "Double")

hotel.tambah_kamar(kamar1)
hotel.tambah_kamar(kamar2)

pelanggan = Pelanggan("John Doe")

reservasi = hotel.buat_reservasi(pelanggan, 101)
if reservasi:
    print(f"Kamar {reservasi.kamar.nomor} berhasil dipesan untuk {reservasi.pelanggan.nama}")
else:
    print("Reservasi gagal")
