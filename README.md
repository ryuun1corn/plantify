# Plantify ☘

## URL PWS: http://yudayana-arif-plantify.pbp.cs.ui.ac.id/ 

## Penjelasan

### Cara saya mengimplementasikan checklist yaitu dengan:
    1. Membuat proyek baru dengan menginisasi Python Virtual Environment baru untuk memisahkan package dan dependensi dari proyek, kemudian dilanjut dengan membuat proyek Django bernama "plantify" menggunakan command line tool yang dimiliki oleh Django itu sendiri.
    2. Pembuatan aplikasi dengan nama 'main' dilakukan dengan menggunakan command line tool Django juga, yaitu dengan command startapp diikuti dengan nama aplikasinya yaitu 'main' untuk membuat sebuah folder yaitu app main.
    3. Routing proyek dimulai dengan menambahkan host-host tertentu seperti localhost dan URL PWS untuk memberi akses ke aplikasi melalui endpoint tersebut, kemudian dilakukan modifikasi terhadap urls.py di folder aplikasi utama dan folder aplikasi main. Saya memutuskan untuk meletakkan aplikasi main di dalam rute 'home/'.
    4. Membuat model di aplikasi main dilakukan dengan memodifikasi file models.py yang terdapat dalam folder main. Setiap atribut dalam model tersebut juga telah diberikan tipe data yang sesuai dengan atributnya.
    5. Untuk mengembalikan template HTML yang sudah dibuat di aplikasi main, perlu ditambahkan fungsi di dalam file views.py yang akan mengatur rendering file HTML statis sesuai dengan konteks yang sudah diberikan di dalam fungsi tersebut juga. Di konteks tersebut, saya tambahkan nama aplikasi, nama saya, npm saya, dan kelas pbp yang saya ambil.
    6. Kemudian untuk menyocokkan url terhadap fungsi yang sudah dibuat, saya melakukan routing di file urls.py di dalam folder main untuk menjalankan fungsi di views.py jika sub-URL di aplikasi main tersebut terkena request pada segmen ''. Sehingga fungsi tersebut akan jalan jika diminta path 'home/'.
    7. Deployment ke PWS saya lakukan dengan membuat proyek baru di website PWS dan menambahkan URL PWS sebagai salah satu lokasi upstream repo git saya, sehingga saya dapat melakukan deploy aplikasi saya dengan melakukan push menuju upstream URL tersebut yaitu pws.
    8. README.md ini saya buat dengan penjelasan saya sendiri dan bantuan menulis dari cheatsheet markdown.

### Bagan yang berisi request client ke aplikasi web Django serta penjelasan
![bagan](https://github.com/user-attachments/assets/ba5a124a-ede3-428d-9bf0-95c4d9bca242)


### Apa itu git?
Git adalah sebuah software yang berjalan di suatu mesin lokal dan berfungsi menyimpan perubahan-perubahan terhadap suatu proyek pemrograman (tidak selalu).
Dengan ini, terdapat dokumentasi yang lengkap untuk proyek yang dikerjakan serta memungkinkan adanya kolaborasi berbagai pihak dalam proyek tersebut.

### Mengapa framework Django digunakan untuk pembelajaran?
Django dipilih karena sudah terdapat battery di dalamnya yang dapat memudahkan pengembangan aplikasi perangkat lunak dengan mudah dan cepat.
Selain itu, Django sudah memiliki database lengkap dengan ORM yang memungkinkan akses terhadap database dengan lebih intuitif dan cocok bagi pemula.

### Mengapa model Django disebut sebagai ORM?
Model Django disebut ORM (Object-Relational Mapping) karena interaksi aplikasi dengan database tidak menggunakan SQL secara langsung, tetapi menggunakan pemodelan OOP sehingga bersifat lebih intuitif dan lebih aman untuk aplikasi perangkat lunak.



