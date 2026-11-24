from data import *
from utiliti import clear, enter_kembali, pilih_divisi, konfirmasi, menu_user
from prettytable import PrettyTable
from colorama import Fore, Style
from datetime import datetime


def cari_pendaftar(nim):
    for pendaftar in data_pendaftars_divisi:
        if pendaftar["nim"] == nim:
            return pendaftar
    return None


def daftar_divisi(nama, nim):
    clear()

    print("\n=== DAFTAR DIVISI MAKRAB ===")

    tabel_divisi = PrettyTable()
    tabel_divisi.field_names = ["No", "Divisi", "Kuota Awal"]

    for i, divisi in enumerate(DAFTAR_DIVSI):
        tabel_divisi.add_row([
            i + 1,
            divisi,
            kuota_divisi[divisi]
        ])

    print(tabel_divisi)

    print("\nKuota hanya sebagai informasi.")
    print("Kuota belum berkurang sebelum Admin menerima pendaftar.")

    print("\n=== PILIH 3 DIVISI ===")

    pilihan_divisi = []

    pilihan_1 = pilih_divisi("Pilih DIVISI PRIORITAS 1:", DAFTAR_DIVSI)

    pilihan_divisi.append(pilihan_1)

    pilihan_kedua = [
        divisi for divisi in DAFTAR_DIVSI
        if divisi not in pilihan_divisi
    ]

    pilihan_2 = pilih_divisi(
        "Pilih DIVISI PRIORITAS 2:",
        pilihan_kedua
    )

    pilihan_divisi.append(pilihan_2)
    
    pilihan_ketiga = [
        divisi for divisi in DAFTAR_DIVSI
        if divisi not in pilihan_divisi
    ]

    pilihan_3 = pilih_divisi(
        "Pilih DIVISI PRIORITAS 3:",
        pilihan_ketiga
    )

    pilihan_divisi.append(pilihan_3)

    print("\n=== PILIHAN DIVISI ===")
    print(f"Prioritas 1 : {pilihan_divisi[0]}")
    print(f"Prioritas 2 : {pilihan_divisi[1]}")
    print(f"Prioritas 3 : {pilihan_divisi[2]}")

    while True:
        alasan = input("\nAlasan memilih divisi: ").strip()

        if alasan == "":
            print("Alasan wajib diisi.")
        else:
            break

    portfolio = input(
        "Portfolio (boleh dikosongkan): "
    ).strip()

    print("\n=== KONFIRMASI PENDAFTARAN ===")
    print(f"Divisi 1 : {pilihan_divisi[0]}")
    print(f"Divisi 2 : {pilihan_divisi[1]}")
    print(f"Divisi 3 : {pilihan_divisi[2]}")
    print(f"Alasan  : {alasan}")
    print(f"Portfolio: {portfolio if portfolio else 'Tidak ada'}")

    setuju = konfirmasi(
        "\nApakah data sudah benar? (ya/tidak): "
    )

    if setuju:

        data_baru = {
            "nama": nama,
            "nim": nim,
            "pilihan_divisi": pilihan_divisi,
            "alasan": alasan,
            "portfolio": portfolio,
            "status": "Menunggu Konfirmasi",
            "divisi_diterima": "-",
            "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        data_pendaftars_divisi.append(data_baru)

        print(Fore.GREEN + "\nPendaftaran berhasil disimpan." + Style.RESET_ALL)
        print("Status: Menunggu Konfirmasi")

        enter_kembali()

    else:

        ubah = konfirmasi(
            "Apakah ingin mengubah pilihan divisi? (ya/tidak): "
        )

        if ubah:
            daftar_divisi(nama, nim)
        else:
            print("Pendaftaran dibatalkan.")
            enter_kembali()


def lihat_status(nim):
    clear()

    print("\n=== STATUS PENDAFTARAN ===")

    pendaftar = cari_pendaftar(nim)

    if pendaftar is None:
        print("Status: Belum terdaftar.")
        enter_kembali()
        return

    print(f"Nama               : {pendaftar['nama']}")
    print(f"NIM                : {pendaftar['nim']}")
    print(f"Status             : {pendaftar['status']}")

    print("\nPilihan Divisi:")
    print(f"1. {pendaftar['pilihan_divisi'][0]}")
    print(f"2. {pendaftar['pilihan_divisi'][1]}")
    print(f"3. {pendaftar['pilihan_divisi'][2]}")

    print(f"\nDivisi Diterima    : {pendaftar['divisi_diterima']}")
    print(f"Tanggal Pendaftaran: {pendaftar['tanggal']}")

    print("\nPesan Sistem:")

    if pendaftar["status"] == "Menunggu Konfirmasi":
        print("Pendaftaran sedang menunggu konfirmasi Admin.")

    elif pendaftar["status"] == "Diterima":
        print("Selamat! Anda telah diterima sebagai panitia.")

    enter_kembali()


def menu_user_login(nama, nim):
    while True:

        pilihan = menu_user()

        if pilihan == "1":

            pendaftar = cari_pendaftar(nim)

            if pendaftar is not None:
                clear()
                print("\nAnda sudah melakukan pendaftaran.")
                enter_kembali()
            else:
                daftar_divisi(nama, nim)

        elif pilihan == "2":
            lihat_status(nim)

        elif pilihan == "3":
            print(Fore.MAGENTA + "\nAnda berhasil logout." + Style.RESET_ALL)
            enter_kembali()
            break

        else:
            print("Pilihan tidak valid.")
            enter_kembali()