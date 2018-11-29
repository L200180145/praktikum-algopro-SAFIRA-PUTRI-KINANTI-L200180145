#NAMA = SAFIRA PUTRI KINANTI
#NIM = L200180145
#KELAS = D

##Kegiatan 1 Praktikum 9
berkas = open("L200180145","w")
berkas.write("L200180145 \n")
berkas.write("02-08-1999 \n")
berkas.write("Safira Putri Kinanti \n")
berkas.close()

##Kegiatan 2 Praktikum 9
berkas = open("L200180145","w")
berkas.write("L200180145 \n")
berkas.write("Safira Putri Kinanti \n")
berkas.write("Madiun \n")
berkas.write("02-08-1999 \n")
berkas.close()

import shelve
f = open("L200180145","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
TL = f.readline()
f.close()

f = shelve.open("Safira")
f['a'] = [Nama, Asal, TL, Nim]
f.close()

f = shelve.open("Safira")

print f['a'][0]
print f['a'][1]
print f['a'][2]
print f['a'][3]

##Kegiatan 3 praktikum 9
import shelve
f = open("L200180145","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
TL = f.readline()
f.close()

f = shelve.open("Safira")
f['b'] = (Nama, Asal, TL, Nim)
f.close()

##Kegiatan 4 praktikum 9
import shelve
f = shelve.open("Safira")
print 'Nama :' , f['b'][0]
print 'Asal :' , f['b'][1]
print 'TL   :' , f['b'][2]
print 'Nim  :' , f['b'][3]
