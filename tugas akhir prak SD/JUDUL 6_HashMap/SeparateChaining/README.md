# Nomor Telephone
# DESKRIPSI
Proyek ini merupakan implementasi sederhana namun komprehensif dari struktur data Hash Table menggunakan bahasa pemrograman Python. Dalam dunia ilmu komputer, penyimpanan dan pencarian data yang efisien adalah sebuah keharusan, dan algoritma Hash Table menawarkan solusi untuk memproses data tersebut hampir seketika. Kode ini secara khusus memodelkan sebuah buku telepon digital, di mana setiap nama kontak bertindak sebagai kunci(key) pencarian yang akan diubah menjadi indeks numerik melalui sebuah fungsi hash. Indeks numerik inilah yang kemudian menentukan di laci memori mana nomor telepon (value) dari kontak tersebut akan disimpan secara presisi.

Salah satu tantangan utama dalam membangun struktur Hash Table adalah menangani kondisi collision atau tabrakan data—yakni sebuah situasi ketika fungsi matematika secara kebetulan menugaskan dua nama kontak yang berbeda ke dalam laci indeks yang sama. Untuk memecahkan masalah ini, program mengimplementasikan teknik Separate Chaining dengan memanfaatkan konsep Linked List(senarai berantai). Alih-alih menimpa atau menghapus data yang sudah masuk lebih dulu, sistem akan dengan cerdas merangkaikan data baru pada laci memori yang mengalami tabrakan. Pendekatan ini memastikan bahwa tidak ada informasi kontak yang hilang, sehingga program tetap handal dalam mengeksekusi operasi inti seperti penambahan(insert), pencarian(search), pembaruan data(update), dan penghapusan(delete) dengan terstruktur.
# SOURCE CODE
<img width="684" height="449" alt="image" src="https://github.com/user-attachments/assets/6c7b23d7-8224-4430-95e1-a3a4f9c49d5c" />
<img width="681" height="442" alt="image" src="https://github.com/user-attachments/assets/708f9612-74b9-432f-a234-11f60d9c9323" />
<img width="674" height="446" alt="image" src="https://github.com/user-attachments/assets/e3037501-e502-49e3-b8ac-e945f5d8a37a" />

# PENJELASAN CODE
Kode ini dibangun menggunakan pendekatan pemrograman berorientasi objek yang terdiri dari dua blok utama yaitu cetak biru untuk wadah data dan pengelola tabelnya. Wadah data ini bertugas sebagai elemen terkecil yang menyimpan informasi secara individual. Di dalam setiap wadah ini tersimpan nama kontak sebagai kunci pencarian, nomor telepon sebagai nilai data, dan sebuah penunjuk arah yang pada awalnya dibiarkan kosong. Penunjuk arah inilah yang nantinya menjadi komponen paling krusial untuk mengikat dan merangkaikan beberapa data sekaligus apabila sistem terpaksa menempatkan mereka di ruang memori yang sama akibat terjadinya tabrakan indeks perhitungan.

Sebagai pengelola utama dari seluruh proses tersebut, sistem menyiapkan sebuah deretan ruang penyimpanan berwujud array dengan ukuran kapasitas tertentu yang semuanya disiapkan dalam keadaan kosong pada saat program pertama kali dijalankan. Untuk menentukan di ruang mana sebuah wadah data harus diletakkan, sistem mengandalkan sebuah rumus matematis internal. Rumus ini bekerja secara sistematis dengan menjumlahkan nilai karakter numerik dari setiap ejaan huruf pada nama kontak. Hasil penjumlahan dari huruf huruf tersebut kemudian dibagi dengan total ukuran kapasitas memori untuk diambil nilai sisa baginya, sehingga program bisa menjamin bahwa setiap data selalu mendapatkan ruang yang presisi dan tidak pernah terlempar keluar dari batas penyimpanan yang ada.

Proses interaksi datanya juga dirancang agar dapat berjalan dengan sangat teliti melalui mekanisme penelusuran berantai. Saat pengguna mencoba memasukkan nama kontak baru, program akan memeriksa ruang memori yang dituju. Jika ruang tersebut sudah terisi oleh rantai data lain, program akan menelusurinya untuk memastikan apakah nama yang sama sudah pernah dicatat sebelumnya, di mana sistem cukup menimpa nomor telepon lamanya saja jika nama tersebut ditemukan. Namun jika nama itu benar benar baru, program akan menyisipkan wadah data tersebut pada posisi paling depan dan menyambungkannya dengan data lama yang sudah ada di belakangnya. Pola penelusuran rantai yang berurutan ini juga diterapkan persis saat pengguna ingin mencari nomor telepon seseorang atau ketika ingin menghapus sebuah catatan kontak secara permanen dari dalam memori penyimpanan.

# OUTPUT
<img width="630" height="290" alt="image" src="https://github.com/user-attachments/assets/8fd7879d-6413-467c-81d8-69eeade14f3f" />

# LINK YOUTUBE

https://youtu.be/oxcLdtNZhIk
