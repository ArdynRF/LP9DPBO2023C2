from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_wifi(self):
        return "Tersedia"
    
    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nWifi : " + self.get_wifi()
    
    def get_photo(self):
        return "kos.jpg"