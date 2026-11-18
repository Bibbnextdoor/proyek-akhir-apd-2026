data_akun = [
    {
        "nama": "ferdika",
        "nim": "039",
        "password": "039",
        "role": "admin"
    },
    {
        "nama": "habibur",
        "nim": "045",
        "password": "045",
        "role": "admin"
    }
]

# Contoh data dummy pendaftar (sebagai referensi, tidak digunakan oleh program):
# data_akun = [
#     {
#         "nama": "Budi Santoso",
#         "nim": "123456789",
#         "pilihan_divisi": ["ACARA", "HUMAS", "KONSUMSI"],
#         "alasan": [],
#         "status": "Menunggu Konfirmasi",
#         "divisi_diterima": "-",
#         "tanggal": "01-01-2026 10:00"
#     }
# ]

data_pendaftars_divisi = []

data_daftar_divisi = [
    "ACARA",
    "HUMAS",
    "KEAMANAN",
    "KESEHATAN",
    "DANUS",
    "KONSUMSI",
    "PDD",
    "PERLENGKAPAN",
    "DEKORASI"
]

kuota_divisi = {
    "ACARA": 0,
    "HUMAS": 1,
    "KEAMANAN": 0,
    "KESEHATAN": 0,
    "DANUS": 0,
    "KONSUMSI": 0,
    "PDD": 0,
    "PERLENGKAPAN": 0,
    "DEKORASI": 0
}