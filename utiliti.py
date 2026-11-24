import os
from prettytable import PrettyTable
from colorama import Fore, Style
import inquirer

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def enter_kembali():
    input(Fore.GREEN + "\nTekan ENTER untuk kembali..." + Style.RESET_ALL)

def enter_ulang():
    input(Fore.GREEN + "\nTekan ENTER untuk mencoba ulang..." + Style.RESET_ALL)

def menu_utama():
    clear()

    tabel_menu = PrettyTable()
    tabel_menu.field_names = [Fore.YELLOW + "No", "Menu" + Style.RESET_ALL]
    tabel_menu.align = "l"

    tabel_menu.add_row(["1", "Login"])
    tabel_menu.add_row(["2", "Registrasi Akun"])
    tabel_menu.add_row(["3", "Keluar Program"])

    print("\n=== SISTEM PENDAFTARAN MAKRAB INFORMATIKA 2026 ===")
    print(tabel_menu)

    pilihan = input("Pilih menu: ").strip()

    return pilihan


def menu_user():
    clear()

    tabel_menu = PrettyTable()
    tabel_menu.field_names = [Fore.YELLOW + "No", "Menu" + Style.RESET_ALL]

    tabel_menu.align = "l"

    tabel_menu.add_row(["1", "Daftar Divisi"])
    tabel_menu.add_row(["2", "Lihat Status Pendaftaran"])
    tabel_menu.add_row(["3", "Logout"])

    print("\n=== MENU USER ===")
    print(tabel_menu)

    return input("Pilih menu: ").strip()


def menu_admin():
    clear()

    tabel_menu = PrettyTable()
    tabel_menu.field_names = [
        Fore.YELLOW + "No",
        "Menu" + Style.RESET_ALL
    ]

    tabel_menu.align = "l"

    tabel_menu.add_row(["1", "Lihat Daftar Pendaftar"])
    tabel_menu.add_row(["2", "Lihat Sisa Kuota Divisi"])
    tabel_menu.add_row(["3", "Update Divisi Pendaftar"])
    tabel_menu.add_row(["4", "Hapus Data Pendaftar"])
    tabel_menu.add_row(["5", "Grafik Minat Divisi"])
    tabel_menu.add_row(["6", "Logout"])

    print("\n=== MENU ADMIN ===")
    print(tabel_menu)

    return input("Pilih menu: ").strip()


# FUNGSI DENGAN PARAMETER
def pilih_divisi(pesan, daftar_pilihan):
    pertanyaan = [
        inquirer.List(
            "divisi",
            message=pesan,
            choices=daftar_pilihan
        )
    ]

    jawaban = inquirer.prompt(pertanyaan)

    return jawaban["divisi"]

def konfirmasi(pesan):
    while True:
        jawaban = input(pesan).strip().lower()

        if jawaban == "ya":
            return True
        elif jawaban == "tidak":
            return False
        else:
            print("Input tidak valid. Masukkan 'ya' atau 'tidak'.")