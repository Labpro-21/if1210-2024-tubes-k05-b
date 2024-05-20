# IF1210 - Dasar Pemrograman 2024
> Tugas Besar - IF1210 Dasar Pemrograman 2024
Note: main.py dan folder data berada di dalam folder src
# About

Tugas ini meminta dibuatkan program permainan berdasarkan kisah Phineas and Ferb di mana Purry si Platypus (Agent P) ingin menghancurkan monster-monster mengerikan ciptaan Dr. Asep Spakbor, ilmuwan jahat. Monster terbaru Dr. Asep Spakbor terlalu kuat, sehingga Purry membutuhkan bantuan dari agen-agen lainnya. Purry bergegas ke markas rahasia O.W.C.A. (Organisasi Warga Cool Abiez) dan bertemu dengan agen-agen lainnya, yaitu kalian. Purry mengatakan bahwa untuk mengalahkan Dr. Asep Spakbor, kalian harus bekerja sama dan merencanakan strategi yang matang untuk mengalahkan monster-monster kuat tersebut. Kalian siap untuk memulai misi pencarian monster di hutan terpencil yang diyakini sebagai tempat tinggal banyak jenis monster, menghadapi segala tantangan yang muncul demi keselamatan kota Danville.

# Contributors

1. Abdullah Farhan (19623305)
2. Ahmad Wicaksono (19623245)
3. Shannon Aurellius A. Lie (19623105)
4. B. Alfin Geraldine Baya (16523175)
5. Bryan R. Ryanto Purba (16523045)


# Features

1. Register
2. Login
3. Logout
3. Menu & Help
4. Inventory
5. Battle
6. Arena
7. Shop & Currency (Potion/ Monster)
8. Laboratory
9. Shop Management
10. Monster Management
11. Save
12. Exit
13. Jackpot

# How to Run

1. Ketikkan python main.py {nama folder csv di dalam folder data} di terminal untuk menjalankan program.
   Misalnya: python main.py cobab

2. Saat layar selamat datang muncul, ketik help untuk menampilkan daftar perintah yang dapat digunakan.

3. Untuk mendaftarkan pengguna dan menyimpan datanya, lakukan registrasi terlebih dahulu dengan mengetik register, lalu masukkan username dan password.

4. Pilih monster awal dari daftar yang ditampilkan dengan mengetik angka yang sesuai dengan nama monster tersebut.

5. Login dengan mengetik login, kemudian masukkan username dan password yang telah Anda daftarkan.

6. Ketik help untuk melihat daftar perintah yang tersedia, kemudian pilih tindakan yang ingin Anda lakukan.

7. Untuk perintah inventory, akan menampilkan informasi tentang inventaris kita, termasuk jumlah koin yang dimiliki serta detail monster dan potion yang  
   tersedia. Ketik nomor monster untuk melihat spesifikasinya secara detail. Untuk kembali ke menu utama, ketikkan keluar.
   gambar inventory

8. Dalam perintah battle, akan ditampilkan daftar monster yang Anda miliki. Anda dapat memilih nomor monster yang ingin Anda gunakan untuk bertarung. Setelah 
   itu, level monster lawan akan dipilih secara acak. Anda memiliki pilihan untuk menyerang dengan memasukkan angka 1, menggunakan ramuan dengan angka 2, atau keluar dari pertarungan 3. Jika Anda menang, Anda akan mendapatkan koin dan pertarungan akan berakhir. Namun, jika Anda kalah, anda tidak mendapat apa apa.

9. Dalam perintah arena, akan ditampilkan monster yang akan menjadi lawan untuk berlatih. Pengguna dapat memilih monster yang ingin dilatih dari daftar yang 
   tersedia. Level monster lawan akan disesuaikan stage yang ditempuh oleh pegguna. Jika di stage 1, level monsternya adalah 1 dan ssterusnya. Pengguna memiliki opsi untuk menyerang dengan memilih angka 1, menggunakan ramuan dengan memilih angka 2, atau keluar dari pertandingan dan melihat riwayat pertandingan dengan memilih angka 3. Jika pengguna menang, mereka akan memperoleh koin dan pertandingan akan berlanjut hingga mereka kalah atau menang melawan semua lawan, dengan maksimal 5 pertandingan. Namun, jika pengguna kalah, akan ditampilkan riwayat pertandingan.

10. Dalam perintah shop_currency, Jika anda sebagai Agent terdapat opsi untuk melakukan pembelian monster atau potion. Anda bisa mengetik "beli", lalu pilih 
    "monster" jika ingin membeli monster, atau "potion" untuk membeli ramuan (pastikan koin Anda mencukupi). Untuk kembali ke menu utama, ketik "keluar".

11. Dalam perintah shop_management, Jika Anda berperan sebagai admin, Anda memiliki keistimewaan untuk meninjau semua barang yang tersedia di toko, memperbarui 
    stok dan harga, menghapus atau menambahkan barang. Tekan "keluar" untuk kembali ke menu utama.

12. Dalam perintah laboratory, Anda memiliki opsi untuk meningkatkan level monster yang Anda miliki dengan membayar biaya yang ditentukan. Pilih nomor monster 
    yang ingin Anda tingkatkan levelnya, serta level yang diinginkan. Untuk kembali ke menu utama, ketikkan keluar.

13. Dalam perintah jackpot, akan ditampilkan daftar item beserta harganya yang bisa dimainkan untuk memenangkan koin OC secara gratis. Pastikan koin OC Anda 
    mencukupi sebelum memainkan permainan ini.

14. Perintah save akan menyimpan data pengguna yang telah bermain game ini ke dalam suatu folder di dalam folder data.

15. Dengan menggunakan perintah logout, akun pengguna akan keluar dari permainan, sehingga pengguna kehilangan akses dari akun sebelumnya. Namun, pengguna masih 
    bisa kembali bermain dengan login atau mendaftar akun baru.

16. Dalam perintah exit, pengguna akan diminta untuk mengonfirmasi apakah mereka ingin menyimpan progres terkini. Jika pengguna memilih 'y', progres akan 
    disimpan. Jika memilih 'n', progres tidak akan disimpan. Setelah itu, pengguna akan keluar dari program.



