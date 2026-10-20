# ============================================
# TODO-CLI — Manajemen tugas sederhana di terminal
# ============================================
# Jalankan:
#   python todo.py
#
# Data disimpan di tasks.json (satu folder dengan file ini) supaya
# tidak hilang saat program ditutup.
# ============================================

import json
from pathlib import Path

FILE_TUGAS = Path(__file__).parent / "tasks.json"


class Tugas:
    def __init__(self, teks: str):
        self.teks = teks
        self.selesai = False

    def selesaikan(self) -> None:
        self.selesai = True

    def to_dict(self) -> dict:
        return {"teks": self.teks, "selesai": self.selesai}

    def __str__(self) -> str:
        status = "x" if self.selesai else " "
        return f"[{status}] {self.teks}"


# --- Persistence ---
def simpan_tugas(daftar: list[Tugas]) -> None:
    data = [t.to_dict() for t in daftar]
    with open(FILE_TUGAS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def muat_tugas() -> list[Tugas]:
    try:
        with open(FILE_TUGAS, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    daftar = []
    for item in data:
        t = Tugas(item["teks"])
        t.selesai = item["selesai"]
        daftar.append(t)
    return daftar


# --- Tampilan ---
def tampilkan_daftar(daftar: list[Tugas], judul: str = "Daftar Tugas") -> None:
    print(f"\n--- {judul} ---")
    if not daftar:
        print("(kosong)")
        return
    for i, tugas in enumerate(daftar, start=1):
        print(f"{i}. {tugas}")


def tampilkan_semua(daftar: list[Tugas]) -> None:
    tampilkan_daftar(daftar, "Semua Tugas")


def tampilkan_belum_selesai(daftar: list[Tugas]) -> None:
    belum = [t for t in daftar if not t.selesai]
    tampilkan_daftar(belum, "Belum Selesai")


def tampilkan_selesai(daftar: list[Tugas]) -> None:
    selesai = [t for t in daftar if t.selesai]
    tampilkan_daftar(selesai, "Sudah Selesai")


def cari_tugas(daftar: list[Tugas]) -> None:
    kata = input("Cari kata kunci: ").strip().lower()
    if not kata:
        print("Kata kunci tidak boleh kosong.")
        return
    hasil = [t for t in daftar if kata in t.teks.lower()]
    tampilkan_daftar(hasil, f"Hasil pencarian '{kata}'")


# --- Aksi ---
def tambah_tugas(daftar: list[Tugas]) -> None:
    teks = input("Teks tugas baru: ").strip()
    if not teks:
        print("Teks tugas tidak boleh kosong.")
        return
    daftar.append(Tugas(teks))
    simpan_tugas(daftar)
    print(f"Ditambahkan: {teks}")


def ambil_nomor(daftar: list[Tugas], aksi: str) -> int | None:
    """Minta nomor tugas yang valid (1..len(daftar)) atau None kalau salah."""
    if not daftar:
        print("Belum ada tugas.")
        return None

    tampilkan_daftar(daftar)
    try:
        nomor = int(input(f"Nomor tugas yang ingin {aksi}: ").strip())
    except ValueError:
        print("Nomor harus berupa angka.")
        return None

    if not 1 <= nomor <= len(daftar):
        print("Nomor tugas tidak valid.")
        return None
    return nomor


def selesaikan_tugas(daftar: list[Tugas]) -> None:
    nomor = ambil_nomor(daftar, "diselesaikan")
    if nomor is None:
        return
    daftar[nomor - 1].selesaikan()
    simpan_tugas(daftar)
    print(f"Selesai: {daftar[nomor - 1].teks}")


def hapus_tugas(daftar: list[Tugas]) -> None:
    nomor = ambil_nomor(daftar, "dihapus")
    if nomor is None:
        return
    tugas = daftar.pop(nomor - 1)
    simpan_tugas(daftar)
    print(f"Dihapus: {tugas.teks}")


# --- Menu ---
def tampilkan_menu() -> None:
    print("\n===== TODO-CLI =====")
    print("1. Lihat semua tugas")
    print("2. Lihat yang belum selesai")
    print("3. Lihat yang sudah selesai")
    print("4. Tambah tugas")
    print("5. Tandai selesai")
    print("6. Hapus tugas")
    print("7. Cari tugas")
    print("8. Keluar")


def main() -> None:
    daftar = muat_tugas()
    aksi = {
        1: tampilkan_semua,
        2: tampilkan_belum_selesai,
        3: tampilkan_selesai,
        4: tambah_tugas,
        5: selesaikan_tugas,
        6: hapus_tugas,
        7: cari_tugas,
    }

    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-8): ").strip())
        except ValueError:
            print("Pilihan harus berupa angka.")
            continue

        if pilihan == 8:
            print("Sampai jumpa!")
            break
        if pilihan in aksi:
            aksi[pilihan](daftar)
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
