# ── Singly Linked List ──

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.rear = None

    def create_new_node(self, n):
        return Node(n)

    def insert_at_beg(self, new_node):
        if self.start is None:
            self.start = self.rear = new_node
        else:
            new_node.next = self.start
            self.start = new_node

    def insert_at_end(self, new_node):
        if self.start is None:
            self.start = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def delete_node(self):
        if self.start is None:
            print("List kosong (underflow)!")
        else:
            deleted = self.start.data
            self.start = self.start.next
            if self.start is None:
                self.rear = None
            print(f"Node {deleted} dihapus.")

    def display(self):
        if self.start is None:
            print("(kosong)")
            return
        current = self.start
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ── Doubly Linked List ──

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.rear = None

    def create_new_node(self, n):
        return DNode(n)

    def insert_node(self, new_node):
        if self.start is None:
            self.start = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def traverse_forward(self):
        print("Traversal maju: ", end="")
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        print("Traversal mundur: ", end="")
        current = self.rear
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


# ── Main ──

def singly():
    ll = LinkedList()
    print("\n=== Singly Linked List ===")
    choice = 'y'
    while choice.lower() == 'y':
        try:
            c = int(input("Nilai baru = "))
        except ValueError:
            print("Masukkan angka!")
            continue

        new_node = ll.create_new_node(c)
        print("1. Sisipkan di depan")
        print("2. Sisipkan di belakang")
        try:
            pos = int(input("Pilihan: "))
        except ValueError:
            pos = 1

        if pos == 2:
            ll.insert_at_end(new_node)
            print("Node dimasukkan di akhir.")
        else:
            ll.insert_at_beg(new_node)
            print("Node dimasukkan di awal.")

        print("List: ", end="")
        ll.display()
        choice = input("Tambah node lagi? (y/n) ")

    while True:
        print("List: ", end="")
        ll.display()
        d = input("Hapus node pertama? (y/n) ")
        if d.lower() == 'y':
            ll.delete_node()
        else:
            break


def doubly():
    dll = DoublyLinkedList()
    print("\n=== Doubly Linked List ===")
    choice = 'y'
    while choice.lower() == 'y':
        try:
            c = int(input("Nilai baru = "))
        except ValueError:
            print("Masukkan angka!")
            continue

        new_node = dll.create_new_node(c)
        dll.insert_node(new_node)
        print("Node ditambahkan.")
        choice = input("Tambah node lagi? (y/n) ")

    print("1. Traversal maju")
    print("2. Traversal mundur")
    try:
        arah = int(input("Pilihan: "))
    except ValueError:
        arah = 1

    if arah == 2:
        dll.traverse_backward()
    else:
        dll.traverse_forward()


if __name__ == "__main__":
    print("== Percobaan 2: Linked List ==")
    print("1. Singly Linked List")
    print("2. Doubly Linked List")
    try:
        pilih = int(input("Pilihan: "))
    except ValueError:
        pilih = 1

    if pilih == 2:
        doubly()
    else:
        singly()
