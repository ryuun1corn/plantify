# <center>Plantify :deciduous_tree:</center>

<center>
    <a href="http://yudayana-arif-plantify.pbp.cs.ui.ac.id/" target="_blank">
        yudayana-arif-plantify.pbp.cs.ui.ac.id
    </a>
    <br>
</center>
<br>

> :sunflower: **Reminder:** Have you watered your plants today?

---

### Jawaban Tugas :three:

<details open>
    <summary>Lihat disini</summary>

##### 1. Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?

Data delivery dibutuhkan dalam implementasi sebuah platform agar dapat tercipta sebuah app yang bersifat dinamik, interaktif, dan dapat membawa pengalaman yang menyesuaikan kepada pengguna platform.

Dengan data delivery, sebuah aplikasi dapat menerima dan menyimpan data yang diberikan oleh pengguna, membuka banyak kemungkinan terhadap fitur-fitur yang dapat dibawa oleh aplikasi tersebut.

##### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, kedua format tersebut memiliki kelebihan dan kekurangannya masing-masing. Tetapi untuk kebanyakan aplikasi modern, JSON adalah format yang lebih populer dan umum digunakan.

Hal ini dikarenakan format JSON yang menggunakan pasangan key-value untuk menyimpan data sehingga lebih mudah untuk dibaca dibandingkan dengan XML yang menggunakan opening dan closing tags, membuat isinya lebih sulit untuk dibaca.

Akibat dari sintaksnya yang lebih simpel, JSON juga secara umum memiliki ukuran file yang lebih kecil jika dibandingkan dengan XML, sehingga _data delivery_ dapat berjalan dengan lebih lancar dan dengan performa yang lebih baik.

Walaupun JSON memang pilihan terbaik secara umum, XML masih memiliki kelebihan dari JSON di situasi tertentu, seperti saat dibutuhkan format dokumen yang lebih kompleks atau saat diperlukannya metadata dari sebuah dokumen.

##### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` berfungsi untuk melakukan validasi terhadap data form yang sudah disubmit ke dalam form tersebut. Method tersebut dijalankan setiap sebuah request dikirim melalui form, memastikan bahwa data yang dimasukkan sesuai dengan apa yang seharusnya diterima.

> Contoh:
>
> > Di form aplikasi Plantify terdapat field yaitu 'price' yang menerima input berupa integer.
> > Apabila input yang dimasukkan berupa huruf alfabet, maka form tidak akan menyimpan datanya, tetapi melempar sebuah error terhadap field 'price' tersebut.

##### 4. Mengapa kita membutuhkan 'csrf_token' saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan 'csrf_token' pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

'csrf_token' pada form Django berfungsi untuk meningkatkan keamanan dari interaksi antara pengguna dengan aplikasi yang sedang digunakannya. Lebih spesifik lagi, token tersebut berfungsi untuk menghindari serangan CSRF (Cross Site Request Forgery).

Serangan CSRF adalah sebuah serangan dimana sang penyerang dapat memanfaatkan kredensial autentikasi pengguna aplikasi untuk mengirim request di luar kendali si pengguna. Hal ini dilakukan dengan mencantumkan cookies dari sesi autentikasi yang dimiliki oleh pengguna kepada request yang dikirim oleh si penyerang, sehingga aplikasi menganggap bahwa request tersebut datang dari si pengguna (bukan penyerang).

'csrf_token' dapat menanggulangi kejadian ini dengan melakukan generasi token csrf unik di form yang ingin disubmit. Kemudian saat sebuah request dikirim, Django dapat menyocokkan token yang dikirim dengan yang sudah ada pada aplikasi untuk memastikan bahwa request tersebut datang dari sumber yang terpercaya (yaitu formnya).

Token ini berbeda dengan cookies yang menyimpan data sesi autentikasi karena token ini diletakkan di form yang diberikan kepada pengguna, sehingga penyerang tidak dapat mengakses form ini dengan trik licik. Tanpa adanya token ini, aplikasi tidak dapat memastikan bahwa request yang diterima memang datang dari si pengguna atau rekayasa sang penyerang.

##### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya. <br>

  1. Membuat sebuah class untuk form input data

  ```python
  class TropicalPlantEntryForm(ModelForm):
      class Meta:
          model = TropicalPlant
          fields = ["name", "price", "description", "weight"]
  ```

  2. Membuat fungsi untuk menampilkan dan menerima data submit dari form berdasarkan class form yang sudah dibuat sebelumnya

  ```python
  def add_tropical_plant(request):
      form = TropicalPlantEntryForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
          form.save()
          return redirect("main:show_main")

      context = {"form": form}
      return render(request, "add_tropical_plant.html", context)
  ```

  3. Menambahkan URL yang menampilkan form tersebut

  ```python
  urlpatterns = [
      ...
      path("add-tropical-plant/", add_tropical_plant, name="add_tropical_plant"),
  ]
  ```

  4. Membuat template HTML untuk form input yang akan diberikan ke pengguna

  ```html
  {% extends 'base.html' %} {% block content %}
  <h1>Add New Tropical Plant</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td>
          <input type="submit" value="Add Tropical Plant" />
        </td>
      </tr>
    </table>
  </form>

  {% endblock %}
  ```

- [x] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. <br>
      Fungsi-fungsi di bawah ini ditambahkan di file views.py untuk menampilkan data yang terdapat dalam aplikasi. Data disediakan dalam format JSON atau XML, dan dalam jumlah banyak atau hanya satu saja.

  ```python
  def get_tropical_plants_xml(request):
      plants = TropicalPlant.objects.all()
      return HttpResponse(
          serializers.serialize("xml", plants), content_type="application/xml"
      )


  def get_tropical_plants_json(request):
      plants = TropicalPlant.objects.all()
      return HttpResponse(
          serializers.serialize("json", plants), content_type="application/json"
      )


  def get_tropical_plant_xml(request, id):
      plant = TropicalPlant.objects.filter(pk=id)
      return HttpResponse(
          serializers.serialize("xml", plant), content_type="application/xml"
      )


  def get_tropical_plant_json(request, id):
      plant = TropicalPlant.objects.filter(pk=id)
      return HttpResponse(
          serializers.serialize("json", plant), content_type="application/json"
      )
  ```

- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2. <br>
      URL ditambahkan di file urls.py di dalam folder main untuk mengakses views yang ada pada poin 2.
  ```python
  urlpatterns = [
      ...
      path(
          "tropical-plant-xml/", get_tropical_plants_xml, name="get_tropical_plants_xml"
      ),
      path(
          "tropical-plant-json/",
          get_tropical_plants_json,
          name="get_tropical_plants_json",
      ),
      path(
          "tropical-plant-xml/<str:id>/",
          get_tropical_plant_xml,
          name="get_tropical_plant_xml",
      ),
      path(
          "tropical-plant-json/<str:id>/",
          get_tropical_plant_json,
          name="get_tropical_plant_json",
      ),
  ]
  ```

#### Screenshot Insomnia dari URL
- XML All
![xml](https://github.com/user-attachments/assets/9a933278-4d8f-40e3-9edb-65edae18e54d)
- XML One
![xml-spec](https://github.com/user-attachments/assets/05fb2c9c-73f8-428b-872f-fbea0afb9b18)
- JSON All
![json](https://github.com/user-attachments/assets/46f02245-2422-4c29-b721-0fc76f55e60e)
- JSON One
![json-spec](https://github.com/user-attachments/assets/2632d1e0-86e9-4df3-988a-1fb5e9b8a2f6)


</details>

---

### Jawaban Tugas :two:

<details>
    <summary>Lihat disini</summary>

### <ins>1. Cara saya mengimplementasikan checklist yaitu dengan</ins>:

1. Membuat proyek baru dengan menginisasi Python Virtual Environment baru untuk memisahkan package dan dependensi dari proyek, kemudian dilanjut dengan membuat proyek Django bernama "plantify" menggunakan command line tool yang dimiliki oleh Django itu sendiri.
2. Pembuatan aplikasi dengan nama 'main' dilakukan dengan menggunakan command line tool Django juga, yaitu dengan command startapp diikuti dengan nama aplikasinya yaitu 'main' untuk membuat sebuah folder yaitu app main.
3. Routing proyek dimulai dengan menambahkan host-host tertentu seperti localhost dan URL PWS untuk memberi akses ke aplikasi melalui endpoint tersebut, kemudian dilakukan modifikasi terhadap urls.py di folder aplikasi utama dan folder aplikasi main. Saya memutuskan untuk meletakkan aplikasi main di dalam rute 'home/'.
4. Membuat model di aplikasi main dilakukan dengan memodifikasi file models.py yang terdapat dalam folder main. Setiap atribut dalam model tersebut juga telah diberikan tipe data yang sesuai dengan atributnya.
5. Untuk mengembalikan template HTML yang sudah dibuat di aplikasi main, perlu ditambahkan fungsi di dalam file views.py yang akan mengatur rendering file HTML statis sesuai dengan konteks yang sudah diberikan di dalam fungsi tersebut juga. Di konteks tersebut, saya tambahkan nama aplikasi, nama saya, npm saya, dan kelas pbp yang saya ambil.
6. Kemudian untuk menyocokkan url terhadap fungsi yang sudah dibuat, saya melakukan routing di file urls.py di dalam folder main untuk menjalankan fungsi di views.py jika sub-URL di aplikasi main tersebut terkena request pada segmen ''. Sehingga fungsi tersebut akan jalan jika diminta path 'home/'.
7. Deployment ke PWS saya lakukan dengan membuat proyek baru di website PWS dan menambahkan URL PWS sebagai salah satu lokasi upstream repo git saya, sehingga saya dapat melakukan deploy aplikasi saya dengan melakukan push menuju upstream URL tersebut yaitu pws.
8. README.md ini saya buat dengan penjelasan saya sendiri dan bantuan menulis dari cheatsheet markdown.

### <ins>2. Bagan yang berisi request client ke aplikasi web Django serta penjelasan</ins>

![bagan](https://github.com/user-attachments/assets/ba5a124a-ede3-428d-9bf0-95c4d9bca242)

### <ins>3. Apa itu git</ins>?

Git adalah sebuah software yang berjalan di suatu mesin lokal dan berfungsi menyimpan perubahan-perubahan terhadap suatu proyek pemrograman (tidak selalu).
Dengan ini, terdapat dokumentasi yang lengkap untuk proyek yang dikerjakan serta memungkinkan adanya kolaborasi berbagai pihak dalam proyek tersebut.

### <ins>4. Mengapa framework Django digunakan untuk pembelajaran</ins>?

Django dipilih karena sudah terdapat battery di dalamnya yang dapat memudahkan pengembangan aplikasi perangkat lunak dengan mudah dan cepat.
Selain itu, Django sudah memiliki database lengkap dengan ORM yang memungkinkan akses terhadap database dengan lebih intuitif dan cocok bagi pemula.

### <ins>5. Mengapa model Django disebut sebagai ORM?</ins>

Model Django disebut ORM (Object-Relational Mapping) karena interaksi aplikasi dengan database tidak menggunakan SQL secara langsung, tetapi menggunakan pemodelan OOP sehingga bersifat lebih intuitif dan lebih aman untuk aplikasi perangkat lunak.

</details>
