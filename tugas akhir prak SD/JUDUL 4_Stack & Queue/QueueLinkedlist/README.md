# ANTREAN BANK
# DESKRIPSI
Kode ini merupakan sebuah implementasi lengkap dari sistem manajemen antrean kasir yang dibangun menggunakan bahasa pemrograman Python dengan memanfaatkan struktur data fundamental dalam ilmu komputer, yaitu Linked List. Program ini dirancang untuk mensimulasikan secara digital bagaimana sebuah antrean pelanggan di kasir bekerja dalam kehidupan nyata, mulai dari proses seorang pelanggan mendaftarkan dirinya ke dalam antrean, hingga proses pemanggilan pelanggan tersebut untuk dilayani oleh kasir, serta kemampuan untuk memantau kondisi dan kepadatan antrean secara langsung.

Secara arsitektur, program ini dibangun di atas dua pilar utama, yakni dua buah class (kelas) yang masing-masing memiliki tanggung jawab yang berbeda namun saling berkaitan erat. Class pertama bernama Node, yang bertugas sebagai representasi atomik dari setiap individu pelanggan dalam antrean. Class kedua bernama AntreanKasir, yang berperan sebagai manajer atau pengendali utama dari keseluruhan struktur antrean, mengelola bagaimana node-node pelanggan tersebut dihubungkan, ditambahkan, dan dihapus secara terstruktur dan efisien.

Filosofi inti yang mendasari cara kerja program ini adalah prinsip FIFO (First In, First Out)  siapa yang datang lebih dulu, dialah yang akan dilayani lebih dulu. Prinsip ini sangat selaras dengan ekspektasi sosial dalam kehidupan sehari-hari ketika seseorang mengantri di kasir supermarket, bank, rumah sakit, atau fasilitas publik lainnya. Dengan mengimplementasikan prinsip ini secara digital, program memastikan keadilan dan keteraturan dalam proses pelayanan.
Dari sisi teknis, alasan dipilihnya Linked List sebagai struktur data utama  bukan array atau list biasa Python  adalah karena linked list unggul dalam operasi penambahan elemen di akhir (enqueue) dan penghapusan elemen di depan (dequeue) yang keduanya dapat dilakukan dalam kompleksitas waktu O(1) atau konstan, selama pointer depan dan belakang selalu dijaga dengan benar. Hal ini menjadikan program sangat efisien secara komputasi meskipun jumlah pelanggan bertambah banyak, karena tidak perlu menggeser elemen seperti halnya pada array konvensional.

Program ini berinteraksi dengan pengguna melalui antarmuka CLI (Command Line Interface) berbasis menu teks yang sederhana namun fungsional. Pengguna disajikan empat pilihan aksi utama yang dapat dilakukan kapan saja secara berulang: mendaftarkan pelanggan baru ke antrean, memanggil pelanggan yang berada paling depan untuk dilayani kasir, melihat seluruh kondisi dan isi antrean saat ini, serta menutup program kasir. Sistem ini juga dilengkapi dengan fitur peringatan otomatis yang akan aktif ketika jumlah pelanggan dalam antrean mencapai ambang batas lima orang atau lebih, memberikan sinyal kepada operator kasir bahwa kondisi antrean mulai padat dan pelayanan perlu dipercepat.

Secara keseluruhan, program ini bukan sekadar latihan akademis dalam memahami struktur data, melainkan juga merupakan prototipe fungsional yang merepresentasikan logika bisnis nyata dalam pengelolaan antrean, dan dapat dikembangkan lebih lanjut menjadi sistem yang lebih kompleks dengan tambahan fitur seperti nomor antrean otomatis, estimasi waktu tunggu, antrean prioritas, hingga integrasi dengan antarmuka grafis atau sistem berbasis web.

# SOURCE CODE
<img width="511" height="427" alt="image" src="https://github.com/user-attachments/assets/b8ad5be2-0e6c-4ec0-bd60-b33756a1c067" />
<img width="532" height="410" alt="image" src="https://github.com/user-attachments/assets/fda74984-3e35-48b1-8f23-73fc6d1b499b" />
<img width="572" height="410" alt="image" src="https://github.com/user-attachments/assets/16f80dbf-f74e-47ec-804f-50b6793ad90e" />

# PENJELASAN CODE
<img width="275" height="79" alt="image" src="https://github.com/user-attachments/assets/f71583b2-99fd-41d7-bb92-db7896f1e062" />
Class Node adalah unit terkecil dan paling fundamental dalam keseluruhan sistem ini. Setiap kali seorang pelanggan baru mendaftarkan diri ke dalam antrean, sebuah objek Node baru akan diciptakan untuk merepresentasikan keberadaan pelanggan tersebut di dalam struktur data. Class ini hanya memiliki dua atribut, namun keduanya sangat krusial.
Atribut pertama, self.nama, berfungsi sebagai identitas unik dari setiap pelanggan. Nilai ini menyimpan string nama yang diinputkan oleh pengguna program dan akan digunakan sepanjang siklus hidup node tersebut dalam antrean mulai dari saat pelanggan masuk, ditampilkan dalam daftar antrean, hingga dipanggil oleh kasir.
Atribut kedua, self.lanjut, adalah pointer atau penunjuk yang merupakan jantung dari mekanisme linked list itu sendiri. Atribut ini menyimpan referensi ke objek Node berikutnya dalam rantai antrean. Nilai awalnya diset None, yang berarti ketika sebuah node baru pertama kali dibuat, ia belum mengetahui siapa yang ada di belakangnya. Hubungan antar node baru akan terbentuk ketika node tersebut resmi disambungkan ke dalam struktur antrean melalui method masuk_antrean.

<img width="254" height="106" alt="image" src="https://github.com/user-attachments/assets/d2184ed5-71ec-4c9d-8a39-f4e87793955a" />

Class AntreanKasir adalah otak dan pengendali pusat dari seluruh operasi sistem antrean ini. Ia bertanggung jawab penuh atas pengelolaan struktur linked list yang menampung semua node pelanggan. Ketika objek dari class ini pertama kali dibuat melalui perintah antrean = AntreanKasir(), konstruktor __init__ langsung menginisialisasi tiga atribut penting yang menjadi fondasi operasional sistem.
Atribut self.depan adalah pointer yang selalu menunjuk ke node paling awal dalam antrean, yaitu pelanggan yang sudah menunggu paling lama dan berhak untuk dilayani lebih dahulu. Pointer inilah yang akan dirujuk setiap kali kasir ingin memanggil pelanggan berikutnya.
Atribut self.belakang adalah pointer yang selalu menunjuk ke node paling akhir dalam antrean, yaitu posisi di mana pelanggan baru akan disambungkan ketika mereka mendaftarkan diri. Dengan menjaga pointer ini, sistem dapat menambahkan pelanggan baru ke ujung antrean secara langsung tanpa harus menelusuri seluruh rantai linked list dari awal.
Atribut self.jumlah adalah pencacah integer yang secara real-time merekam berapa banyak pelanggan yang sedang berada dalam antrean pada suatu momen. Nilai ini selalu diperbarui setiap kali ada pelanggan yang masuk atau dipanggil, dan digunakan sebagai parameter untuk menentukan status kepadatan antrean.

<img width="520" height="245" alt="image" src="https://github.com/user-attachments/assets/4f413b83-c4dd-4757-8bac-76af45f2ab3c" />
Method masuk_antrean mengimplementasikan operasi enqueue, yaitu proses penambahan elemen baru ke bagian paling belakang antrean. Ini adalah salah satu dari dua operasi inti dalam struktur data queue. Proses yang terjadi di balik layar ketika method ini dipanggil sangatlah terstruktur dan efisien.
Langkah pertama adalah instansiasi node baru — objek Node baru diciptakan dengan nama pelanggan yang diberikan sebagai parameter. Node ini pada awalnya berdiri sendiri, belum terhubung ke node manapun dalam antrean.
Langkah kedua adalah penentuan kondisi antrean melalui percabangan logika. Jika self.depan is None, artinya antrean saat ini benar-benar kosong dan node baru ini adalah pelanggan pertama. Dalam kondisi ini, baik pointer depan maupun belakang keduanya akan langsung menunjuk ke node baru tersebut, karena node ini sekaligus menjadi yang pertama sekaligus yang terakhir. Namun jika antrean sudah memiliki isi, node baru disambungkan ke atribut lanjut dari node yang saat ini berada paling belakang, lalu pointer belakang digeser maju untuk menunjuk ke node baru tersebut.
Setelah proses penyambungan selesai, counter jumlah dinaikkan satu angka, konfirmasi teks dicetak ke layar, dan sistem secara otomatis memeriksa apakah jumlah antrean telah menyentuh atau melampaui ambang batas lima orang untuk menampilkan peringatan kepadatan.

<img width="547" height="178" alt="image" src="https://github.com/user-attachments/assets/1c6aa682-7864-489f-bd83-25b2b9909cc2" />
Setelah pemanggilan, pointer self.depan digeser maju untuk menunjuk ke node berikutnya dalam rantai, yaitu self.depan.lanjut. Dengan cara ini, pelanggan yang baru saja dipanggil secara efektif.

.<img width="361" height="324" alt="image" src="https://github.com/user-attachments/assets/97da5fa4-46d3-44a9-b756-b8f4c2e55587" />

Method lihat_antrean melakukan operasi traversal terhadap keseluruhan linked list dari ujung depan hingga ujung belakang, lalu menampilkan hasilnya dalam format visual yang mudah dipahami. Traversal adalah teknik penelusuran linked list dengan mengikuti rantai pointer lanjut dari satu node ke node berikutnya hingga mencapai None.

# OUTPUT

<img width="432" height="454" alt="image" src="https://github.com/user-attachments/assets/f2fbaa08-90d7-4083-9f81-f964388106d0" />

<img width="356" height="197" alt="image" src="https://github.com/user-attachments/assets/63aba1c0-0844-4205-90e5-7c8393807295" />


# LINK YOUTUBE

https://youtu.be/DI4TQxP34Jw
