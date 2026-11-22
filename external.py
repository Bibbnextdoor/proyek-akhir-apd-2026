
import json
import os

LOKASI_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def simpan_data(data_akun, data_pendaftar, kuota_divisi):

    data = {
        "data_akun": data_akun,
        "data_pendaftar": data_pendaftar,
        "kuota_divisi": kuota_divisi
    }

    with open(LOKASI_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def muat_data():

    if os.path.exists(LOKASI_FILE):

        with open(LOKASI_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    return None
