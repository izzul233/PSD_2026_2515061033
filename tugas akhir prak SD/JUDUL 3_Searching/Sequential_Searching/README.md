# PENCARIAN CEPAT PEMENANG GIVEAWAY
# DESKRIPSI
Proyek kecil ini berisi contoh sederhana penerapan algoritma Sequential Search atau Pencarian Berurutan menggunakan bahasa pemrograman Python. Konsep utamanya dibungkus dalam simulasi pencarian nama pemenang giveaway dari sebuah daftar peserta. Layaknya kita mencari nama seseorang di selembar kertas absen dari urutan paling atas hingga paling bawah, algoritma ini akan mengecek setiap data di dalam list secara berurutan. Jika nama target sudah berhasil ditemukan di tengah jalan, program akan cerdas mengambil jalan pintas dengan menghentikan proses pencarian secara langsung menggunakan perintah break. Hal ini membuat program bekerja lebih efisien karena tidak perlu membuang waktu untuk mengecek sisa nama di urutan selanjutnya. Sebaliknya, jika pencarian sudah mencapai akhir daftar namun nama target tetap tidak ada, program akan otomatis menginformasikan bahwa peserta tersebut tidak ditemukan.

Kode dalam repositori ini sengaja dirancang agar sangat ramah bagi pemula. Tidak ada penggunaan struktur sintaks yang rumit seperti function (def) ataupun class, melainkan murni mengandalkan alur logika dasar sehari-hari. Tujuannya adalah agar teman-teman yang baru saja mulai belajar Python bisa dengan mudah memahami bagaimana cara kerja perulangan ketika digabungkan dengan logika pengkondisian (if statement). Intinya, repositori ini tidak bertujuan untuk membuat aplikasi yang kompleks, melainkan sebagai wadah belajar untuk memahami pondasi paling awal tentang bagaimana sebuah komputer memproses dan mencari data di dalam kumpulan informasi.
# SOURCE CODE
<img width="1069" height="614" alt="image" src="https://github.com/user-attachments/assets/e05527ee-0ea6-4ade-ae12-cff0e6d83f66" />
# PENJELASAN CODE
<img width="747" height="52" alt="image" src="https://github.com/user-attachments/assets/2989fc8d-bd46-4501-9bc9-a29f7b34c468" />
yang pertama saya menampilkan pencarian cepat pemenang giveaway sebagai tema dari code tersebut
<img width="953" height="152" alt="image" src="https://github.com/user-attachments/assets/e7d9092c-a265-4163-8d84-2d4a259effca" />
selanjutnya adalah membuat nama daftar peserta,di situ nama pesertanya adalah ahmad,budi,cici,danang,elis,dan fajar
selanjutnya adalah nama peserta yang di cari,nama yang di cari adalah danang
selanjutnya adalah sudah_ketemu = false,kenapa false? karena untuk pencarian pertama itu tidak munhgkin langsung ketemu maka dari itu dia false,dan ketika sudah ketemu dia akan true
lalu tampilkan mencari nama danang di dalam daftar
<img width="1184" height="243" alt="image" src="https://github.com/user-attachments/assets/b875bca4-1d36-492b-abd4-36d2ee51c03d" />
selanjutnya adalah fungsi perulangan,bekerja dengan cara mengecek satu persatu di dalam daftar peserta tersebut dengan menampilkan mengecek urutan ke- orang yang di
lalu agar pengurutannya tidak di mulai dari 0 maka kita menggunakan urutan + 1
cek,jika nama yang di cek itu sudah ketemu maka dia akan menampilkan "pemenang di temukan" lalu menampilkan juga "pemenang atas nama danang ada di ururtan ke-4 lalu sudah ketemu akan true lalu break 
<img width="368" height="49" alt="image" src="https://github.com/user-attachments/assets/6885c9bf-a4d3-4810-b0e8-42b43bf7af47" />
lalu dia akan menampilkan pencarian selesai
<img width="986" height="150" alt="image" src="https://github.com/user-attachments/assets/ebcb85af-8b6e-48ae-80da-e4c4ad297197" />
jika nama yang di cari itu tidak ada dalam daftar nama peserta,maka dia akan menampilkan nama {nama_dicari} tidak ditemukan di daftar peserta,lalu pencarian selesai.
# OUTPUT
<img width="620" height="279" alt="image" src="https://github.com/user-attachments/assets/631ca07b-890d-4124-93e9-fcfe580ecf63" />
output program ini menampilkan proses kerja komputer langkah demi langkah. Saat dijalankan, layar akan memunculkan satu per satu nama yang sedang dicek dari urutan paling awal, mulai dari ahmad, budi, cici, hingga sampai ke danang. Begitu target "danang" dicek dan ternyata cocok, program akan langsung mencetak pesan keberhasilan bahwa pemenang ditemukan beserta keterangan posisinya di dalam daftar yaitu urutan ke-4. Karena pemenang sudah berhasil didapatkan, pencarian akan otomatis berhenti di titik tersebut. Alhasil, nama-nama sisa yang ada di daftar bawahnya, seperti elis dan fajar, tidak akan diproses atau dimunculkan lagi di layar.
# LINK YOUTUBE
https://youtu.be/BJoS0tGAGqA
