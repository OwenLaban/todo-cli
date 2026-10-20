# ✅ todo-cli

Manajemen tugas sederhana langsung dari terminal — Python, tanpa dependensi eksternal.

## Masalah

Mencatat tugas harian sering kali butuh aplikasi berat atau akun online. Untuk
kebutuhan sederhana, CLI sudah cukup: cepat dibuka, data tersimpan lokal, dan
tidak butuh internet.

## Fitur

- Tambah, tandai selesai, dan hapus tugas
- Filter: semua tugas, belum selesai, sudah selesai
- Cari tugas berdasarkan kata kunci
- Data tersimpan otomatis di `tasks.json` (tidak hilang saat program ditutup)
- Input divalidasi: pilihan menu bukan angka, nomor tidak valid, teks kosong

## Demo

```text
===== TODO-CLI =====
1. Lihat semua tugas
2. Lihat yang belum selesai
3. Lihat yang sudah selesai
4. Tambah tugas
5. Tandai selesai
6. Hapus tugas
7. Cari tugas
8. Keluar
Pilih menu (1-8): 1

--- Semua Tugas ---
1. [x] Belajar OOP
2. [ ] Latihan file I/O
```

## Cara Menjalankan

Butuh Python 3.10+ (dikembangkan dengan Python 3.13.5).

```sh
git clone https://github.com/OwenLaban/todo-cli.git
cd todo-cli
python todo.py
```

Tidak ada dependensi eksternal — cukup Python standar.

## Struktur

```text
todo-cli/
├── todo.py        # seluruh aplikasi: class, persistence, fitur, menu
├── tasks.json     # data tugas (dibuat otomatis, tidak di-commit)
├── .gitignore
└── README.md
```

## Cara Kerja

1. `class Tugas` menyimpan teks dan status selesai.
2. Daftar tugas disimpan sebagai list of dict di `tasks.json`.
3. Setiap perubahan langsung ditulis ke file (`simpan_tugas`).
4. Saat program dibuka, data dibaca kembali (`muat_tugas`) — dengan
   penanganan `FileNotFoundError` kalau file belum ada.
5. Menu memakai **dict dispatch** `{nomor: fungsi}` agar penambahan menu
   tidak membuat rantai `if/elif` makin panjang.

## Keterbatasan

- Single user dan lokal — belum sinkron antar perangkat
- Belum ada due date, prioritas, atau kategori
- Belum ada test otomatis (menyusul di Minggu 5)

## Yang Dipelajari

- Python: OOP, file I/O, JSON, error handling, type hints, list comprehension
- Git: init, commit bertahap, branch, pull request, merge
- Menulis README yang menjelaskan masalah, cara jalan, dan keterbatasan
