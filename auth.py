from data import *
from utiliti import clear, enter_kembali, enter_ulang
from pwinput import pwinput
from colorama import Fore, Style
from pendaftaran import menu_user_login
from admin import menu_admin_login
from external import simpan_data
import re

def cari_akun(nim):
    for akun in data_akun:
        if akun["nim"] == nim:
            return akun
    return None

def login():
    for percobaan in range(3, 0, -1):
        clear()
        print("\n=== LOGIN ===")
        
        nim = input("NIM: ").strip()
        password = pwinput("Password: ").strip()

        akun = cari_akun(nim)

        if akun is None:
            print(Fore.RED + "\nLogin gagal." + Style.RESET_ALL)
            print("NIM tidak ditemukan.")

        elif akun["password"] != password:
            print(Fore.RED + "\nLogin gagal." + Style.RESET_ALL)
            print("Password salah.")

        else:
            if akun["role"] == "admin":
                print(Fore.GREEN + f"\nSelamat datang, {akun['nama']}! ke menu admin" + Style.RESET_ALL)
                input("\nTekan ENTER untuk masuk ke menu...")
                menu_admin_login()

            elif akun["role"] == "user":
                print(Fore.GREEN + f"\nSelamat datang, {akun['nama']}! ke menu pendaftaran" + Style.RESET_ALL)
                input("\nTekan ENTER untuk masuk ke menu...")                
                menu_user_login(akun["nama"], akun["nim"])
            
            return

        if percobaan > 1:
            enter_ulang()
    
    clear()
    print(Fore.RED + "\nAnda telah gagal login 3 kali." + Style.RESET_ALL)
    print("Silakan mencoba kembali dari menu utama.")
    enter_kembali()    

def register():
    clear()

    print("\n=== REGISTRASI AKUN ===")

    while True:
        try:
            print("Masukan Nama Lengkap atau kembali")
            nama = input("Nama lengkap: ").strip()

            if nama.lower() == "kembali":
                return
            
            if not re.match(r"^[a-zA-Z\s']+$", nama):
                raise ValueError("Nama tidak boleh kosong atau Input hanya boleh huruf, spasi, dan tanda petik satu (')!.\n")
                    
        except ValueError as e:
            print(e)    
        else: 
            break    

    while True:
        try:
            print("Masukan NIM atau kembali")
            nim = input("NIM lengkap: ").strip()

            if nim.lower() == "kembali":
                return
            
            if nim == "":
                raise ValueError("NIM tidak boleh kosong.")
            elif not nim.isdigit():
                raise ValueError("NIM hanya boleh angka.")
                

            for akun in data_akun:
                if akun["nim"] == nim:
                    raise ValueError("NIM sudah terdaftar. Gunakan NIM lain.")
        
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try: 
            print("Masukan Password atau kembali")
            password = pwinput("Password: ").strip()

            if password.lower() == "kembali":
                return
            
            if password == "":
                raise ValueError("Password tidak boleh kosong.")
        except ValueError as e:
            print(e)
        else:
            break

    akun_baru = {"nama": nama, "nim": nim, "password": password, "role": "user"}

    data_akun.append(akun_baru)
    
    berhasil = simpan_data(data_akun, data_pendaftars_divisi, kuota_divisi)

    if berhasil:
        print(Fore.GREEN + "\nRegistrasi berhasil!" + Style.RESET_ALL)
        print("Akun berhasil dibuat sebagai User.")

    else:
        data_akun.pop()

        print(Fore.RED + "\nRegistrasi gagal disimpan." + Style.RESET_ALL)
        print("Data akun dikembalikan. Silakan mencoba kembali.")
        
    enter_kembali()