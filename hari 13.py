class Film:
    def __init__(self, judul, durasi):
        self.judul = judul
        self.durasi = durasi

class Kursi:
    def __init__(self, nomor):
        self.nomor = nomor
        self.tersedia = True

    def pesan(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

class Tiket:
    def __init__(self, film, kursi):
        self.film = film
        self.kursi = kursi

class Bioskop:
    def __init__(self):
        self.film_list = []
        self.kursi_list = [Kursi(i) for i in range(1, 101)] # 100 kursi

    def tambah_film(self, film):
        self.film_list.append(film)

    def cari_film(self, judul):
        for film in self.film_list:
            if film.judul == judul:
                return film
        return None

    def pesan_tiket(self, judul_film, nomor_kursi):
        film = self.cari_film(judul_film)
        if film:
            kursi = self.kursi_list[nomor_kursi - 1]
            if kursi.pesan():
                return Tiket(film, kursi)
        return None

# Contoh penggunaan
bioskop = Bioskop()
film1 = Film("Avengers: Endgame", 180)
film2 = Film("Inception", 148)

bioskop.tambah_film(film1)
bioskop.tambah_film(film2)

tiket = bioskop.pesan_tiket("Inception", 5)
if tiket:
    print(f"Tiket berhasil dipesan untuk film {tiket.film.judul} di kursi nomor {tiket.kursi.nomor}")
else:
    print("Pemesanan tiket gagal")
