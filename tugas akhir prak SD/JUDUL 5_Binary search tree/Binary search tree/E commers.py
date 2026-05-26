from collections import deque

class Node:
    def __init__(self, id_produk):
        self.key = id_produk  
        self.left = None
        self.right = None

class BSTGudang:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def successor(self, key):
        current = self.root
        succ = None

        while current:
            if key < current.key:
                succ = current
                current = current.left
            else:
                current = current.right

        return succ.key if succ else None

    def predecessor(self, key):
        current = self.root
        pred = None

        while current:
            if key > current.key:
                pred = current
                current = current.right
            else:
                current = current.left
        return pred.key if pred else None

    def min_node(self, root):
        current = root

        while current.left:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)

        elif key > root.key:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_node(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def level_order(self):
        if self.root is None:
            print("Gudang kosong (tidak ada produk).")
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        print()


def main():
    gudang = BSTGudang()
    pilih = 0

    while pilih != 5:

        print("\n=== MANAJEMEN GUDANG E-COMMERS ===")
        print("1. Tambah ID Produk baru ke gudang")
        print("2. Cari ID Produk terdekat yang lebih besar")
        print("3. Cari ID Produk terdekat yang lebih kecil")
        print("4. Hapus ID Produk & Tampilkan Struktur Rak")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            nomor = int(input("Masukkan ID Produk baru: "))
            gudang.insert(nomor)
            print(f"Produk dengan ID {nomor} berhasil didaftarkan ke rak.")

        elif pilih == 2:
            nomor = int(input("Masukkan ID Produk yang dicek: "))
            hasil = gudang.successor(nomor)

            if hasil is not None:
                print(f"ID Produk terdekat yang lebih besar dari {nomor} adalah: {hasil}")
            else:
                print("Tidak ada produk dengan ID yang lebih besar di gudang ini.")

        elif pilih == 3:
            nomor = int(input("Masukkan ID Produk yang dicek: "))
            hasil = gudang.predecessor(nomor)

            if hasil is not None:
                print(f"ID Produk terdekat yang lebih kecil dari {nomor} adalah: {hasil}")
            else:
                print("Tidak ada produk dengan ID yang lebih kecil di gudang ini.")

        elif pilih == 4:
            nomor = int(input("Masukkan ID Produk yang ingin dihapus (Stok Habis): "))
            gudang.delete(nomor)
            print(f"ID Produk {nomor} telah dihapus dari sistem gudang.")

            print("Struktur posisi penempatan produk terbaru (Atas ke Bawah):")
            gudang.level_order()

        elif pilih == 5:
            print("Sistem gudang ditutup. Terima kasih.")

        else:
            print("Pilihan menu tidak valid!")


if __name__ == "__main__":
    main()