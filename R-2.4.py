class Flower:
    def __init__(self, nama, jumlah_kelopak,harga):
        self.nama = nama
        self.jumlah_kelopak = jumlah_kelopak
        self.harga = harga
    
    def set_nama(self, new_nama):
        self.nama = new_nama

    def set_jumlah_kelopak(self, new_jumlah_kelopak):
        self.jumlah_kelopak = new_jumlah_kelopak
    
    def iklan(self):
        print("Bunga " + self.nama + " berkelopak {}".format(self.jumlah_kelopak) + " harganya {}".format(self.harga))

flower1 = Flower("Asoka", 15, 5000)
flower2 = Flower("Mawar", 7, 7000)
print("Bunga" , flower1.nama , "berkelopak" , flower1.jumlah_kelopak , "harganya" , flower1.harga)
flower1.iklan()
flower2.iklan()