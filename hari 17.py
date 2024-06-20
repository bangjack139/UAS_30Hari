class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.selesai = False

    def tandai_selesai(self):
        self.selesai = True

class PengelolaTugas:
    def __init__(self):
        self.tugas_list = []

    def tambah_tugas(self, tugas):
        self.tugas_list.append(tugas)

    def hapus_tugas(self, tugas):
        self.tugas_list.remove(tugas)

    def tampilkan_tugas(self):
        for tugas in self.tugas_list:
            status = "Selesai" if tugas.selesai else "Belum Selesai"
            print(f"{tugas.deskripsi} - {status}")

# Contoh penggunaan
pengelola = PengelolaTugas()
tugas1 = Tugas("Belajar Python")
tugas2 = Tugas("Mengerjakan PR Matematika")

pengelola.tambah_tugas(tugas1)
pengelola.tambah_tugas(tugas2)

# Tampilkan semua tugas
pengelola.tampilkan_tugas()

# Tandai tugas selesai
tugas1.tandai_selesai()

# Tampilkan semua tugas setelah satu tugas selesai
pengelola.tampilkan_tugas()
