class Node:
    def __init__(self, name, phone):
        self.name  = name
        self.phone = phone  
        self.next  = None

class PhoneBookSeparateChaining:
    def __init__(self, size=7):
        self.size  = size
        self.table = [None] * size

    def _hash(self, name):
        return sum(ord(c) for c in name) % self.size
    
    def insert(self, name, phone):
        idx  = self._hash(name)
        curr = self.table[idx]
        while curr:              
            if curr.name == name:
                curr.phone = phone   
                print(f"[UPDATE] '{name}' -> slot {idx}")
                return
            curr = curr.next
        new_node      = Node(name, phone)
        new_node.next = self.table[idx]
        self.table[idx] = new_node
        print(f"[INSERT] '{name}' -> slot {idx}")

    def search(self, name):
        idx  = self._hash(name)
        curr = self.table[idx]
        while curr:
            if curr.name == name:
                return curr.phone
            curr = curr.next
        return None
    
    def delete(self, name):
        idx  = self._hash(name)
        curr = self.table[idx]
        prev = None
        while curr:
            if curr.name == name:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[idx] = curr.next
                return True
            prev, curr = curr, curr.next
        return False
    
    def display(self):
        print("\n=== ISI TABEL ===")
        for i in range(self.size):
            chain, curr = [], self.table[i]
            while curr:
                chain.append(f"({curr.name}, {curr.phone})")
                curr = curr.next
            isi = " -> ".join(chain) if chain else "(kosong)"
            print(f"  [{i}] {isi}")

pb = PhoneBookSeparateChaining(size=5)

pb.insert("Siti",    "081234567890")
pb.insert("Sari",    "082345678901")
pb.insert("Dewi",    "083456789012")
pb.insert("Andi",    "084567890123")
pb.insert("Rudi",    "085678901234")

pb.display()

print("\n=== PENCARIAN ===")
for nama in ["Dewi", "awe", "nina"]:
    hasil = pb.search(nama)
    print(f"  {nama}: {hasil or 'tidak ditemukan'}")

pb.delete("Siti")
print(f"\nSetelah hapus 'Siti': {pb.search('Siti') or 'tidak ada'}")