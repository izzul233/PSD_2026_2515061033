# Data transaksi pengeluaran harian
transaksi = [
    {"nama": "Makan siang",     "jumlah": 45000},
    {"nama": "Transport",       "jumlah": 20000},
    {"nama": "Belanja bulanan", "jumlah": 320000},
    {"nama": "Kopi & snack",    "jumlah": 35000},
    {"nama": "Listrik & air",   "jumlah": 210000},
    {"nama": "Internet",        "jumlah": 150000},
    {"nama": "Parkir",          "jumlah": 10000},
]

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j]["jumlah"] > data[j + 1]["jumlah"]:
                data[j], data[j + 1] = data[j + 1], data[j]  # swap
    return data

def tampilkan(data, judul):
    print(f"\n{'='*40}")
    print(f" {judul}")
    print(f"{'='*40}")
    for i, t in enumerate(data, 1):
        print(f"{i}. {t['nama']:<20} Rp {t['jumlah']:>10,}")
    print(f"{'='*40}")
    print(f"   Total: {'':>20} Rp {sum(t['jumlah'] for t in data):>10,}")

tampilkan(transaksi, "SEBELUM DIURUTKAN")

transaksi_terurut = bubble_sort(transaksi.copy())

tampilkan(transaksi_terurut, "SETELAH DIURUTKAN (Terkecil → Terbesar)")