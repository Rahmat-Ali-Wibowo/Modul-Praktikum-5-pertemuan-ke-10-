# Inisialisasi dictionary daftar kontak
daftar_kontak = {
    "Ari": "081234567890",
    "Dina": "082345678901",
    "Budi": "083456789012"
}

# Tampilkan kontaknya Ari
print(f"Kontak Ari: {daftar_kontak['Ari']}")

# Tambah kontak baru dengan nama Riko, nomor 087654544
daftar_kontak["Riko"] = "087654544"
print("Kontak Riko telah ditambahkan.")

# Ubah kontak Dina dengan nomor baru 088999776
daftar_kontak["Dina"] = "088999776"
print("Kontak Dina telah diperbarui.")

# Tampilkan semua Nama
print("Daftar semua Nama:")
for nama in daftar_kontak.keys():
    print(nama)

# Tampilkan semua Nomor
print("Daftar semua Nomor:")
for nomor in daftar_kontak.values():
    print(nomor)

# Tampilkan daftar Nama dan nomornya
print("Daftar Nama dan Nomornya:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")

# Hapus kontak Dina
del daftar_kontak["Dina"]
print("Kontak Dina telah dihapus.")

# Tampilkan daftar kontak setelah penghapusan
print("Daftar kontak setelah penghapusan Dina:")
for nama, nomor in daftar_kontak.items():
    print(f"{nama}: {nomor}")
