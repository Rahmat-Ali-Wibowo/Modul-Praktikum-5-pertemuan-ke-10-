def hitung_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.35 * uts + 0.35 * uas

# Inisialisasi dictionary daftar nilai mahasiswa
data_mahasiswa = {}

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa[nama] = {
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    }
    print(f"Data untuk {nama} telah ditambahkan.")

def ubah_data():
    nama = input("Masukkan nama mahasiswa yang datanya akan diubah: ")
    if nama in data_mahasiswa:
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_mahasiswa[nama] = {
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        }
        print(f"Data untuk {nama} telah diperbarui.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

def hapus_data():
    nama = input("Masukkan nama mahasiswa yang datanya akan dihapus: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data untuk {nama} telah dihapus.")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

def tampilkan_data():
    if data_mahasiswa:
        print("\nDaftar Data Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"Nama: {nama}, Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Nilai Akhir: {nilai['nilai_akhir']:.2f}")
    else:
        print("Tidak ada data mahasiswa.")

def cari_data():
    nama = input("Masukkan nama mahasiswa yang ingin dicari: ")
    if nama in data_mahasiswa:
        nilai = data_mahasiswa[nama]
        print(f"Nama: {nama}, Tugas: {nilai['tugas']}, UTS: {nilai['uts']}, UAS: {nilai['uas']}, Nilai Akhir: {nilai['nilai_akhir']:.2f}")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

def menu():
    while True:
        print("\nMenu Pilihan:")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Cari Data")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan menu
menu()
