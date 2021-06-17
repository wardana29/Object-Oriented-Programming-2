class Mahasiswa:
     nama="Nurul Niza"

Nurul_Niza=Mahasiswa()#objek dari kelas mahasiswa
print(Nurul_Niza.nama)

print(50*'/') #constraster di panggil setiap objek di buat

class Mahasiswa:
     def __init__(self, nama, umur): #merujuk pada objek ini, ada parameter nama dan umur
          self.nama = nama
          self.umur = umur
     def perkenalan(self):
          print("Hallo nama saya " + self.nama + " Umur saya {}".format(self.umur)) #ini static
class Student:
  pass
mahasiswa1 = Mahasiswa("Mihra", 18) #objek dari kelas mahasiswa
mahasiswa2 = Mahasiswa("Wardana", 19)
print(mahasiswa1.nama)
print(mahasiswa1.umur)

mahasiswa1.perkenalan()
mahasiswa2.perkenalan()

if (mahasiswa1.umur > 17):
     print(Mahasiswa)

mahasiswa1.nama = " ira" #ganti atribute
mahasiswa1.perkenalan()
print(50*'/')

#inheritance
#child class
class MahasiswaPenerimaBeasiswa:
     mahasiswa3 = Mahasiswa(" Yuyun", 19)
     print(mahasiswa3.nama)