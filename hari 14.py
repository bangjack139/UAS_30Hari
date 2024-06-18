class Papan:
    def __init__(self):
        self.papan = [[" " for _ in range(3)] for _ in range(3)]

    def tampilkan_papan(self):
        for baris in self.papan:
            print("|".join(baris))
            print("-" * 5)

    def tempatkan_tanda(self, baris, kolom, tanda):
        if self.papan[baris][kolom] == " ":
            self.papan[baris][kolom] = tanda
            return True
        return False

    def cek_pemenang(self):
        for baris in self.papan:
            if baris[0] == baris[1] == baris[2] != " ":
                return True
        for kolom in range(3):
            if self.papan[0][kolom] == self.papan[1][kolom] == self.papan[2][kolom] != " ":
                return True
        if self.papan[0][0] == self.papan[1][1] == self.papan[2][2] != " ":
            return True
        if self.papan[0][2] == self.papan[1][1] == self.papan[2][0] != " ":
            return True
        return False

class Pemain:
    def __init__(self, nama, tanda):
        self.nama = nama
        self.tanda = tanda

class Permainan:
    def __init__(self, pemain1, pemain2):
        self.papan = Papan()
        self.pemain1 = pemain1
        self.pemain2 = pemain2
        self.giliran = pemain1

    def mainkan(self):
        while True:
            self.papan.tampilkan_papan()
            baris = int(input(f"{self.giliran.nama}, masukkan baris (0-2): "))
            kolom = int(input(f"{self.giliran.nama}, masukkan kolom (0-2): "))
            if self.papan.tempatkan_tanda(baris, kolom, self.giliran.tanda):
                if self.papan.cek_pemenang():
                    self.papan.tampilkan_papan()
                    print(f"{self.giliran.nama} menang!")
                    break
                self.giliran = self.pemain1 if self.giliran == self.pemain2 else self.pemain2
            else:
                print("Tempat sudah diisi, coba lagi.")

# Contoh penggunaan
pemain1 = Pemain("Alice", "X")
pemain2 = Pemain("Bob", "O")

game = Permainan(pemain1, pemain2)
game.mainkan()
