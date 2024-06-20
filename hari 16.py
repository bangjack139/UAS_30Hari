class Siswa:
    def __init__(self, nama, nis):
        self.nama = nama
        self.nis = nis
        self.nilai = {}

    def tambah_nilai(self, mata_pelajaran, nilai):
        self.nilai[mata_pelajaran] = nilai

    def tampilkan_nilai(self):
        for mp, nilai in self.nilai.items():
            print(f"{mp}: {nilai}")

class Guru:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

class MataPelajaran:
    def __init__(self, nama_mp):
        self.nama_mp = nama_mp

class Sekolah:
    def __init__(self):
        self.siswa_list = []
        self.guru_list = []
        self.mapel_list = []

    def tambah_siswa(self, siswa):
        self.siswa_list.append(siswa)

    def tambah_guru(self, guru):
        self.guru_list.append(guru)

    def tambah_mapel(self, mapel):
        self.mapel_list.append(mapel)

    def cari_siswa(self, nis):
        for siswa in self.siswa_list:
            if siswa.nis == nis:
                return siswa
        return None

# Contoh penggunaan
sekolah = Sekolah()
siswa1 = Siswa("Alice", 123)
siswa2 = Siswa("Bob", 456)

guru1 = Guru("Mr. John", 789)

mapel1 = MataPelajaran("Matematika")
mapel2 = MataPelajaran("Bahasa Indonesia")

sekolah.tambah_siswa(siswa1)
sekolah.tambah_siswa(siswa2)
sekolah.tambah_guru(guru1)
sekolah.tambah_mapel(mapel1)
sekolah.tambah_mapel(mapel2)

# Tambah nilai siswa
siswa1.tambah_nilai("Matematika", 85)
siswa1.tambah_nilai("Bahasa Indonesia", 90)

# Tampilkan nilai siswa
siswa1.tampilkan_nilai()
