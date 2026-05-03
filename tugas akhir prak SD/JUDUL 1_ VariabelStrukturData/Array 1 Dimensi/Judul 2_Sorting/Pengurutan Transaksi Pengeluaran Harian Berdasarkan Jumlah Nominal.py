"""
Pengurutan Transaksi Pengeluaran Harian Berdasarkan Jumlah Nominal.
"""

from datetime import date


def insertion_sort(transaksi: list[dict], ascending: bool = True) -> list[dict]:
    """
    Mengurutkan daftar transaksi berdasarkan jumlah nominal.

    Args:
        transaksi : list of dict, setiap dict berisi data transaksi
        ascending : True = dari kecil ke besar, False = dari besar ke kecil

    Returns:
        list transaksi yang sudah diurutkan
    """
    data = transaksi.copy() 
    n = len(data)

    for i in range(1, n):
        kunci = data[i]          
        j = i - 1

        while j >= 0 and (
            (ascending and data[j]["jumlah"] > kunci["jumlah"]) or
            (not ascending and data[j]["jumlah"] < kunci["jumlah"])
        ):
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = kunci     

    return data


def cetak_tabel(judul: str, transaksi: list[dict]) -> None:
    """Menampilkan daftar transaksi dalam format tabel."""
    lebar = 65
    print("\n" + "=" * lebar)
    print(f" {judul}".center(lebar))
    print("=" * lebar)
    print(f"{'No':<4} {'Tanggal':<12} {'Keterangan':<25} {'Jumlah (Rp)':>14}")
    print("-" * lebar)

    total = 0
    for idx, trx in enumerate(transaksi, start=1):
        print(
            f"{idx:<4} "
            f"{trx['tanggal']:<12} "
            f"{trx['keterangan']:<25} "
            f"{trx['jumlah']:>14,.0f}"
        )
        total += trx["jumlah"]

    print("-" * lebar)
    print(f"{'TOTAL':<42} {total:>14,.0f}")
    print("=" * lebar)


def cetak_langkah_insertion_sort(transaksi: list[dict]) -> None:
    """Menampilkan setiap langkah proses Insertion Sort secara detail."""
    data = transaksi.copy()
    n = len(data)

    print("\n" + "=" * 65)
    print(" VISUALISASI LANGKAH-LANGKAH INSERTION SORT".center(65))
    print("=" * 65)
    print("\nData awal (nominal):")
    print([d["jumlah"] for d in data])

    for i in range(1, n):
        kunci = data[i]
        j = i - 1

        print(f"\n--- Iterasi ke-{i} ---")
        print(f"  Elemen kunci : {kunci['keterangan']} = Rp {kunci['jumlah']:,.0f}")

        pergerakan = False
        while j >= 0 and data[j]["jumlah"] > kunci["jumlah"]:
            data[j + 1] = data[j]
            j -= 1
            pergerakan = True

        data[j + 1] = kunci

        if pergerakan:
            print(f"  Disisipkan di posisi ke-{j + 2}")
        else:
            print("  Sudah di posisi yang benar, tidak ada pergeseran.")

        print("  Status array :", [d["jumlah"] for d in data])

    print("\nProses selesai!")


def main():
    transaksi_harian = [
        {"tanggal": "2025-01-03", "keterangan": "Makan siang",       "jumlah": 35_000},
        {"tanggal": "2025-01-03", "keterangan": "Transportasi ojek",  "jumlah": 18_000},
        {"tanggal": "2025-01-03", "keterangan": "Kopi & snack",       "jumlah": 27_500},
        {"tanggal": "2025-01-03", "keterangan": "Listrik token",      "jumlah": 210_000},
        {"tanggal": "2025-01-03", "keterangan": "Internet bulanan",   "jumlah": 150_000},
        {"tanggal": "2025-01-03", "keterangan": "Belanja sayur",      "jumlah": 45_000},
        {"tanggal": "2025-01-03", "keterangan": "Parkir motor",       "jumlah": 5_000},
    ]

    cetak_tabel("DATA TRANSAKSI PENGELUARAN (BELUM DIURUTKAN)", transaksi_harian)

    cetak_langkah_insertion_sort(transaksi_harian)

    hasil_asc = insertion_sort(transaksi_harian, ascending=True)
    cetak_tabel("HASIL PENGURUTAN: TERKECIL → TERBESAR (Ascending)", hasil_asc)

    hasil_desc = insertion_sort(transaksi_harian, ascending=False)
    cetak_tabel("HASIL PENGURUTAN: TERBESAR → TERKECIL (Descending)", hasil_desc)

    nominal_list = [t["jumlah"] for t in transaksi_harian]
    print("\n" + "=" * 65)
    print(" RINGKASAN STATISTIK".center(65))
    print("=" * 65)
    print(f"  Jumlah transaksi  : {len(transaksi_harian)} transaksi")
    print(f"  Pengeluaran terendah  : Rp {min(nominal_list):>12,.0f}")
    print(f"  Pengeluaran tertinggi : Rp {max(nominal_list):>12,.0f}")
    print(f"  Rata-rata pengeluaran : Rp {sum(nominal_list)/len(nominal_list):>12,.0f}")
    print(f"  Total pengeluaran     : Rp {sum(nominal_list):>12,.0f}")
    print("=" * 65)


if __name__ == "__main__":
    main()