from utiliti import menu_utama, clear, enter_kembali
from auth import login, register
from pwinput import pwinput
from colorama import init, Fore, Style


def main():
    init(autoreset=True)
    program_berjalan = True

    while program_berjalan:
        pilihan = menu_utama()

        # LOGIN
        if pilihan == "1":
            login()

        # REGISTER
        elif pilihan == "2":
            register()

        # KELUAR
        elif pilihan == "3":
            clear()

            print(
                Fore.BLUE + "\nTerima kasih telah menggunakan " "Sistem Pendaftaran Makrab Informatika 2026." + Style.RESET_ALL)

            program_berjalan = False

        # INPUT TIDAK VALID
        else:
            print(Fore.RED + "\nPilihan tidak valid." + Style.RESET_ALL)
            enter_kembali()

if __name__ == "__main__":
    main()