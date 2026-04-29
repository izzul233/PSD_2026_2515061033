def menu():
    print("\n--- Array 1 Dimensi ---")
    print("1. Tampilkan address array")
    print("2. Tampilkan address tiap elemen")
    print("3. Isi nilai array")
    print("4. Keluar")

def array_1d():
    a = [0] * 5
    while True:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka!")
            continue

        if choice == 1:
            print(f"Address array: {id(a)}")
        elif choice == 2:
            for i in range(5):
                print(f"Address a[{i}]: {id(a[i])}")
        elif choice == 3:
            print("Masukkan 5 nilai:")
            for i in range(5):
                while True:
                    try:
                        a[i] = int(input(f"  a[{i}] = "))
                        break
                    except ValueError:
                        print("  Input tidak valid!")
            print(f"Array: {a}")
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid.")


def menu_2d():
    print("\n--- Array 2 Dimensi (3x2) ---")
    print("1. Tampilkan address array")
    print("2. Tampilkan address tiap elemen")
    print("3. Isi nilai array")
    print("4. Keluar")

def array_2d():
    b = [[0 for _ in range(2)] for _ in range(3)]
    while True:
        menu_2d()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka!")
            continue

        if choice == 1:
            print(f"Address array: {id(b)}")
        elif choice == 2:
            for i in range(3):
                for j in range(2):
                    print(f"Address b[{i}][{j}]: {id(b[i][j])}")
        elif choice == 3:
            print("Masukkan nilai untuk array 3x2:")
            for i in range(3):
                for j in range(2):
                    while True:
                        try:
                            b[i][j] = int(input(f"  b[{i}][{j}] = "))
                            break
                        except ValueError:
                            print("  Input tidak valid!")
            print("Array sekarang:")
            for row in b:
                print(" ", row)
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    print("--- Percobaan 1: Array ---")
    print("1. Array 1 Dimensi")
    print("2. Array 2 Dimensi")
    try:
        pilih = int(input("Pilihan: "))
    except ValueError:
        pilih = 1

    if pilih == 2:
        array_2d()
    else:
        array_1d()
