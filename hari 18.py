class Rekening:
    def __init__(self, nomor, saldo):
        self.nomor = nomor
        self.saldo = saldo

    def tarik_tunai(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            return True
        return False

    def setor_tunai(self, jumlah):
        self.saldo += jumlah

    def cek_saldo(self):
        return self.saldo

class ATM:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)

    def cari_rekening(self, nomor):
        for rekening in self.rekening_list:
            if rekening.nomor == nomor:
                return rekening
        return None

# Contoh penggunaan
atm = ATM()
rekening1 = Rekening("123456789", 1000000)

atm.tambah_rekening(rekening1)

# Tarik tunai
rekening = atm.cari_rekening("123456789")
if rekening.tarik_tunai(500000):
    print("Penarikan berhasil")
else:
    print("Saldo tidak cukup")

# Setor tunai
rekening.setor_tunai(200000)

# Cek saldo
print(f"Sisa saldo: {rekening.cek_saldo()}")