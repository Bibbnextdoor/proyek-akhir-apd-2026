from data import *
from utiliti import clear, enter_kembali
import pandas as pd
import matplotlib.pyplot as plt

def hitung_pilihan(pilihan, hasil, index=0):

    if index == len(pilihan):
        return hasil

    divisi = pilihan[index]

    if divisi in hasil:
        hasil[divisi] += 1
    else:
        hasil[divisi] = 1

    return hitung_pilihan(pilihan, hasil, index + 1)


def grafik_minat_divisi():
    clear()

    print("\n=== GRAFIK MINAT DIVISI ===")
    if not data_pendaftars_divisi:
        print("Belum ada data pendaftar.")
        enter_kembali()
        return

    hasil = {}

    # Mengambil pilihan 1, 2, dan 3
    for pendaftar in data_pendaftars_divisi:
        pilihan = pendaftar["pilihan_divisi"]

        hasil = hitung_pilihan(pilihan, hasil)

    # Memastikan semua divisi muncul
    for divisi in DAFTAR_DIVSI:
        if divisi not in hasil:
            hasil[divisi] = 0

    data_grafik = {
        "Divisi": list(hasil.keys()),
        "Jumlah Peminat": list(hasil.values())
    }

    dataframe = pd.DataFrame(data_grafik)

    print("\n=== DATA MINAT DIVISI ===")
    print(dataframe)

    plt.figure(figsize=(10, 6))

    plt.bar(
        dataframe["Divisi"],
        dataframe["Jumlah Peminat"]
    )

    plt.title("Grafik Minat Divisi Makrab Informatika 2026")
    plt.xlabel("Divisi")
    plt.ylabel("Jumlah Peminat")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    enter_kembali()