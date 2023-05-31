from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_luas(self):
        return "100 m^2"
    
    def get_photo(self):
        return "apart.jpg"
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas : " + self.get_luas()