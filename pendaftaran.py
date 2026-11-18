from data import * #* artinya semua
from utiliti import clear, enter_kembali, enter_ulang, pilih_divisi, konfirmasi
from prettytable import PrettyTable
from colorama import Fore, Style

def cari_pendaftar(nim):
    for data in data_pendaftars_divisi:
        if data_pendaftar["nim"] == nim:
            return data_pendaftar
        return None
    
def daftar_divisi(nama, nim):
    clear()
    
    print("DAFTAR DIVISI MAKRAB INFORMATIKA 26")
    


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
    
    