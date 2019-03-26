from data import *

def tambah():
	nama = input("nama kontak : ")
	nomor = input("nomor kontak : ")
	contact [nama] = nomor

def hapus():
	hapus = input("nama yang ingin di hapus : ")
	if hapus in contact.keys():
		del contact[hapus]
	else:
		print("tidak ada kontak yang bernama : ", hapus)

def daftar():
	for nama, nomor in contact.items():
		print(nama, nomor)

def cari():
	cari = input("nama yang mau di cari : ")
	no = contact.get(cari)
	if cari in contact.keys():
		print("nomor", cari, "adalah : " , no)
	else:
		print("Maaf ! kontak yang anda cari tidak terdaftar (Belum di input). Terima Kasih.")
