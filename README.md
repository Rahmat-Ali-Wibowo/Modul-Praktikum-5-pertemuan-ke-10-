# Program Mengelola Daftar Nilai Mahasiswa

## Deskripsi
Program ini memungkinkan pengguna untuk mengelola daftar nilai mahasiswa menggunakan dictionary. Pengguna dapat menambah, mengubah, menghapus, menampilkan, dan mencari data mahasiswa. Nilai akhir dihitung berdasarkan komponen nilai tugas, UTS, dan UAS.

## Flowchart
```plaintext
+----------------------------------------------------+
| Mulai                                               |
+----------------------------------------------------+
          |
          v
+---------------------------+
| Inisialisasi dictionary   |
| data_mahasiswa            |
+---------------------------+
          |
          v
+---------------------------+
| Tampilkan menu pilihan    |
| (Tambah, Ubah, Hapus,     |
| Tampilkan, Cari, Keluar)  |
+---------------------------+
          |
          v
+---------------------------+
| Input pilihan pengguna    |
| (1/2/3/4/5/6)             |
+---------------------------+
          |
          v
+-----------------------------+
| Apakah pilihan '1'?         |
| (Tambah Data)               |
+-------------+---------------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+ +-----------+-----------+
| Lanjutkan ke pilihan lain | | Input nama, tugas, UTS,|
| (2/3/4/5/6)               | | UAS                   |
+-------------+-------------+ +-----------------------+
                              | Hitung nilai akhir    |
                              | Tambah data ke list   |
                              +-----------------------+
                                        |
                                        v
+-----------------------------+ +-----------------------+
| Apakah pilihan '2'?         | | Apakah pilihan '3'?   |
| (Ubah Data)                 | | (Hapus Data)          |
+-------------+---------------+ +-------------+---------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+ +-----------+-----------+
| Lanjutkan ke pilihan lain | | Input nama mahasiswa   |
| (3/4/5/6)                 | | Jika ditemukan,        |
+-------------+-------------+ | perbarui data          |
                              +-----------------------+
                                        |
                                        v
+-----------------------------+ +-----------------------+
| Apakah pilihan '4'?         | | Apakah pilihan '5'?   |
| (Tampilkan Data)            | | (Cari Data)           |
+-------------+---------------+ +-------------+---------+
              |Tidak                      |Ya
              v                           v
+-------------+-------------+ +-----------+-----------+
| Lanjutkan ke pilihan lain | | Input nama mahasiswa   |
| (5/6)                     | | Jika ditemukan,        |
+-------------+-------------+ | tampilkan data         |
                              +-----------------------+
                                        |
                                        v
+-----------------------------+
| Apakah pilihan '6'?         |
| (Keluar)                    |
+-------------+---------------+
              |Tidak
              v
+-------------+--------------------+
| Tampilkan menu pilihan lagi      |
| (1/2/3/4/5/6)                    |
+----------------------------------+
              |
              v
+----------------------------------------------------+
| Selesai                                            |
+----------------------------------------------------+
