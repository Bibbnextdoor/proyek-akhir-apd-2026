import json
import os

LOKASI_FILE = os.path.join(os.path.dirname(__file__), "data.json")


def simpan_data(data_akun, data_pendaftars_divisi, kuota_divisi):
    data = {
        "data_akun": data_akun,
        "data_pendaftar": data_pendaftars_divisi,
        "kuota_divisi": kuota_divisi
    }

    try:
        with open(LOKASI_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except (OSError, TypeError, ValueError) as e:
        print(f"Gagal menyimpan data: {e}")
        return False

    else:
        return True


def muat_data():
    if not os.path.exists(LOKASI_FILE):
        return None

    try:
        with open(LOKASI_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    except (OSError, json.JSONDecodeError) as e:
        print(f"Gagal memuat data: {e}")
        return None

    else:
        return data
    