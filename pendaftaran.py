from data import *
from utiliti import clear, enter_kembali, pilih_divisi, konfirmasi, menu_user
from prettytable import PrettyTable
from colorama import Fore, Style
from datetime import datetime
from external import simpan_data


def cari_pendaftar(nim):
    for pendaftar in data_pendaftars_divisi:
        if pendaftar["nim"] == nim:
            return pendaftar
    return None


def daftar_divisi(nama, nim):
    clear()

    print("\n=== DAFTAR DIVISI MAKRAB ===")
    
    ada_divisi = [divisi for divisi in data_daftar_divisi if kuota_divisi[divisi] > 0]
    
    if len(ada_divisi) == 0:
        print("\nMohon maaf, pendaftaran ditutup karena semua kuota divisi sudah penuh.")
        enter_kembali()
        return

    tabel_divisi = PrettyTable()
    tabel_divisi.field_names = ["No", "Divisi", "Kuota Awal"]

    for nomor, divisi in enumerate(ada_divisi):
        tabel_divisi.add_row([
            nomor + 1,
            divisi,
            kuota_divisi[divisi]
        ])

    print(tabel_divisi)

    print("\nKuota hanya sebagai informasi.")
    print("Kuota belum berkurang sebelum Admin menerima pendaftar.")

    print("\n=== PILIH 3 DIVISI ===")

    pilihan_divisi = []
    alasan = []

    pilihan_1 = pilih_divisi("Pilih DIVISI PRIORITAS 1:", ada_divisi)
    pilihan_divisi.append(pilihan_1)

    while True:
        try:
            alasan_1 = input(f"Alasan memilih divisi {pilihan_1}: ").strip()

            if alasan_1 == "":
                raise ValueError("Alasan tidak boleh kosong, wajib diisi")
        except ValueError as e:
            print(e)
        else:
            alasan.append(alasan_1)
            break
            
    pilihan_kedua = [divisi for divisi in ada_divisi if divisi not in pilihan_divisi]

    if len(pilihan_kedua) > 0:
        pilihan_2 = pilih_divisi("Pilih DIVISI PRIORITAS 2:", pilihan_kedua)
        pilihan_divisi.append(pilihan_2)

        while True:
            try:
                alasan_2 = input(f"Alasan memilih divisi {pilihan_2}: ").strip()

                if alasan_2 == "":
                    raise ValueError("Alasan tidak boleh kosong, wajib diisi")
            except ValueError as e:
                print(e)
            else:
                alasan.append(alasan_2)
                break
    
    
    pilihan_ketiga = [divisi for divisi in ada_divisi if divisi not in pilihan_divisi]

    if len(pilihan_ketiga) > 0:
        pilihan_3 = pilih_divisi("Pilih DIVISI PRIORITAS 3:", pilihan_ketiga)
        pilihan_divisi.append(pilihan_3)

        while True:
            try:
                alasan_3 = input(f"Alasan memilih divisi {pilihan_3}: ").strip()

                if alasan_3 == "":
                    raise ValueError("Alasan tidak boleh kosong, wajib diisi")
            except ValueError as e:
                print(e)
            else:
                    alasan.append(alasan_3)
                    break

    print("\n=== KONFIRMASI PENDAFTARAN ===")
    for i in range(len(pilihan_divisi)):
        print(f"Divisi {i+1}: {pilihan_divisi[i]}")
        print(f"Alasan: {alasan[i]}")
    
    setuju = konfirmasi("\nApakah data sudah benar? (ya/tidak): ")

    if setuju:

        data_baru = {
            "nama": nama,
            "nim": nim,
            "pilihan_divisi": pilihan_divisi,
            "alasan": alasan,
            "status": "Menunggu Konfirmasi",
            "divisi_diterima": "-",
            "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        data_pendaftars_divisi.append(data_baru)
        simpan_data(data_akun, data_pendaftars_divisi, kuota_divisi)

        print(Fore.GREEN + "\nPendaftaran berhasil disimpan." + Style.RESET_ALL)
        print("Status: Menunggu Konfirmasi")

        enter_kembali()

    else:

        ubah = konfirmasi("Apakah ingin mengubah pilihan divisi? (ya/tidak): ")

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
    for i in range(len(pendaftar["pilihan_divisi"])):
        print(f"{i+1}. {pendaftar['pilihan_divisi'][i]}")
        print(f"Alasan {pendaftar['pilihan_divisi'][i]}: {pendaftar['alasan'][i]}")

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
            