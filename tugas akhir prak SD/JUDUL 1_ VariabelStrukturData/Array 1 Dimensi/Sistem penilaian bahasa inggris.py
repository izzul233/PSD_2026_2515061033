nama = ["firul", "Ramli", "Siti", "naswa", "Supri"]
nilai = []

print("=" * 40)
print("  SISTEM PENILAIAN BAHASA INGGRIS")
print("=" * 40)

for i in range(len(nama)):
    while True:
        try:
            n = float(input(f"Masukkan nilai {nama[i]}: "))
            if 0 <= n <= 100:
                nilai.append(n)
                break
            else:
                print("Nilai harus antara 0-100.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def get_grade(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "E"

print("\n" + "=" * 40)
print(f"{'No':<4} {'Nama':<10} {'Nilai':<8} {'Grade'}")
print("-" * 40)
for i in range(len(nama)):
    grade = get_grade(nilai[i])
    print(f"{i+1:<4} {nama[i]:<10} {nilai[i]:<8.1f} {grade}")

rata_rata = sum(nilai) / len(nilai)
nilai_max = max(nilai)
nilai_min = min(nilai)
idx_max   = nilai.index(nilai_max)
idx_min   = nilai.index(nilai_min)

print("-" * 40)
print(f"Rata-rata  : {rata_rata:.2f}")
print(f"Nilai tertinggi : {nilai_max} ({nama[idx_max]})")
print(f"Nilai terendah  : {nilai_min} ({nama[idx_min]})")
print("=" * 40)