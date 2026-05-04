def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort_transaksi(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j]['nominal'] > arr[j + 1]['nominal']:
                tukar(arr, j, j + 1)

def main():
    print("=== Program Pengurutan Transaksi Harian ===")
    try:
        n = int(input("Masukkan jumlah transaksi: "))
    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.")
        return
    
    arr = []
    print("\nMasukkan detail transaksi:")
    for i in range(n):
        print(f"\nTransaksi ke-{i+1}")
        nama_transaksi = input("Nama/Deskripsi Transaksi : ")
        
        while True:
            try:
                nominal = float(input("Jumlah Nominal (Rp)      : "))
                arr.append({"nama": nama_transaksi, "nominal": nominal})
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka untuk nominal!")

    print("\n=== Transaksi Sebelum Diurutkan ===")
    for item in arr:
        print(f"- {item['nama']}: Rp{item['nominal']:,.2f}")

    bubble_sort_transaksi(arr, n)

    print("\n=== Transaksi Setelah Diurutkan (Berdasarkan Nominal Terkecil-Terbesar) ===")
    for item in arr:
        print(f"- {item['nama']}: Rp{item['nominal']:,.2f}")

if __name__ == "__main__":
    main()