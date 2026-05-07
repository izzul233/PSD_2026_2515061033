print("=== PENCARIAN CEPAT PEMENANG GIVEAWAY ===")

daftar_peserta = ["ahmad", "budi", "cici", "danang", "elis", "fajar"]
nama_dicari = "danang"
sudah_ketemu = False
print(f"Mencari nama '{nama_dicari}' di dalam daftar...\n")

for urutan in range(len(daftar_peserta)):
    orang_yang_dicek = daftar_peserta[urutan]
    print(f"Mengecek urutan ke-{urutan + 1}: {orang_yang_dicek}")
    if orang_yang_dicek == nama_dicari:
        print("\n Pemenang ditemukan")
        print(f"Pemenang atas nama '{nama_dicari}' ada di urutan ke-{urutan + 1}.")
        sudah_ketemu = True
        break 

if sudah_ketemu == False:
    print(f"\nnama '{nama_dicari}' tidak ditemukan di daftar peserta.")

print("Pencarian selesai.")
