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

### Jawaban Tugas :five:

<details open>
    <summary>Lihat disini</summary>

##### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Aturan pengambilan CSS selector adalah sebagai berikut:

1. Inline styles

Prioritas paling tinggi yang dilihat oleh CSS adalah style yang ditambahkan langsung ke dalam tag html dengan menggunakan atribut style.
Contoh:

```html
<div style="color: red;">Text</div>
```

2. IDs

Prioritas tertinggi kedua adalah IDs, yaitu selector yang memperhatikan atribut ID dari setiap elemen.
Contoh:

```css
#elementID {
  color: blue;
}
```

3. Classes, Attributes, dan Pseudo-classes

Prioritas selanjutnya adalah pemilihan berdasarkan atribut class, atribut lain, dan pseudo-class yang menyatakan keadaan tag tersebut
Contoh:

```css
.className {
  color: green;
}
```

4. Type Selectors and Pseudo-elements

Prioritas terakhir yang dilihat oleh CSS adalah berdasarkan jenis elemen tersebut dan pseudo-element seperti `::before` dan `::after`
Contoh:

```css
p {
  color: yellow;
}
```

##### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design merupakan konsep yang penting dalam pengembangan aplikasi web karena desain yang responsif memungkinkan pengguna untuk mendapatkan kenyamanan yang sama tanpa memedulikan dari mana pengguna mengakses website tersebut.
Dengan adanya responsive design, tampilan web dari berbagai ukuran layar seperti perangkat mobile, tablet, maupun desktop memiliki fungsionalitas yang sama dan tidak mengganggu kepada kenyaman pengguna serta fungsionalitas dari aplikasi tersebut.

Contoh aplikasi yang masih belum menerapkan responsive design akan hanya dapat diakses dari satu jenis ukuran layar saja dan akan terlihat "berantakan" saat diakses dari layar dengan ukuran berbeda:
![Contoh](https://media.licdn.com/dms/image/C4E12AQFUiZXC3Z9rjA/article-cover_image-shrink_600_2000/0/1520161119689?e=2147483647&v=beta&t=y2WsYH06-AFdKv4ffdgOtfVFJYBAy8mi5gytSrgF8Pk)

##### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Ketiga konsep tersebut adalah properti yang sering digunakan untuk mengatur tata ruang dan tampilan elemen HTML. Berikut penjelasan masing-masing:

1. Margin

Margin adalah ruang kosong di luar batasan suatu elemen. Margin bersifat transparan dan digunakan untuk memberi jarak antara elemen tersebut dengan elemen di sekitarnya. Berikut implementasinya di CSS:

```css
element {
  margin: 20px; /* Memberi margin sebesar 20px pada semua sisi */
}

element {
  margin-top: 10px; /* Jarak atas */
  margin-right: 15px; /* Jarak kanan */
  margin-bottom: 20px; /* Jarak bawah */
  margin-left: 25px; /* Jarak kiri */
}
```

2. Border

Border adalah batasan dari suatu elemen HTML itu sendiri, suatu garis yang mengelilingi elemen tersebut dan terletak di antara margin dan padding. Border dapat dilihat oleh pengguna dan dapat diatur warnanya, ketebalannya, dan jenis garinsya. Berikut implementasinya di CSS:

```css
element {
  border: 2px solid black; /* Border dengan ketebalan 2px, tipe garis solid, warna hitam */
}

element {
  border-top: 2px solid red; /* Hanya border atas */
  border-right: 3px dashed blue; /* Hanya border kanan */
}
```

3. Padding

Padding adalah ruang di dalam border, yaitu jarak antara isi atau konten dari elemen dengan border elemen tersebut. Sama seperti margin, padding juga bersifat transparan. Berikut contoh implementasinya dalam CSS:

```css
element {
  padding: 15px; /* Padding sebesar 15px pada semua sisi */
}

element {
  padding-top: 10px; /* Jarak atas */
  padding-right: 15px; /* Jarak kanan */
  padding-bottom: 20px; /* Jarak bawah */
  padding-left: 25px; /* Jarak kiri */
}
```

##### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid adalah dua metode tata letak (layout) di CSS yang berguna untuk mengatur posisi elemen-elemen di halaman web agar lebih fleksibel dan responsif

1. Flexbox

Flexbox dirancang untuk tata letak satu dimensi, yaitu tata letak secara horizontal (baris) atau vertikal (kolom). Flexbox memudahkan pengaturan dan penyelarasan elemen di dalam container tanpa harus menghitung ukuran atau posisi secara manual.

Ini sangat berguna untuk menyusun elemen secara dinamis, di mana elemen-elemen tersebut bisa menyesuaikan diri sesuai ukuran kontainer atau ukuran elemen-elemen lainnya.

2. Grid

Grid adalah metode tata letak dua dimensi yang memungkinkan kita untuk menyusun elemen secara horizontal (baris) dan vertikal (kolom) sekaligus. Ini lebih kompleks daripada Flexbox dan memberikan kendali yang lebih besar untuk menyusun elemen di dalam grid yang terdiri dari baris dan kolom.

Grid memungkinkan untuk membuat desain yang lebih terstruktur, seperti tabel, tetapi dengan fleksibilitas lebih besar dalam pengaturan ukuran dan posisi.

- Kesimpulan

Flexbox lebih cocok untuk mengelola tata letak yang bersifat linier atau satu dimensi, misalnya untuk mengatur elemen dalam baris atau kolom.
Grid lebih cocok untuk tata letak yang melibatkan banyak baris dan kolom dalam struktur yang lebih kompleks.

##### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- [x] Implementasikan fungsi untuk menghapus dan mengedit product.

  Fungsi untuk menghapus dan mengedit product diawali dengan menambahkan kedua fungsi tersebut ke dalam file `views.py`

  ```python
  def edit_tropical_plant(request, id):
  # Get tropical plant berdasarkan ID
      plant = TropicalPlant.objects.get(pk=id)

      # Set Tropical Plant sebagai instance dari form
      form = TropicalPlantEntryForm(request.POST or None, instance=plant)

      if form.is_valid() and request.method == "POST":
      # Simpan form dan kembali ke halaman awal
      form.save()
      return HttpResponseRedirect(reverse("main:show_main"))

      context = {"form": form}
      return render(request, "edit_tropical_plant.html", context)


  def delete_tropical_plant(request, id):
  # Get tropical plant berdasarkan ID
      plant = TropicalPlant.objects.get(pk=id)
      # Hapus plant
      plant.delete()
      # Kembali ke halaman awal
      return HttpResponseRedirect(reverse("main:show_main"))
  ```

  Kemudian menambahkan template HTML baru untuk mengedit entry yang dimiliki

  ```htmldjango
  {% extends 'base.html' %}
  {% block meta %}
      <title>Edit Tropical Plant</title>
  {% endblock meta %}
  {% block content %}
      {% include 'navbar.html' %}
      <section class="min-h-screen flex items-center justify-center w-screen bg-green-100 px-3 md:px-6 pb-6 pt-24">
          <div class="bg-gray-50 rounded-xl form-style p-4 min-w-[50%]">
              <div class="text-center text-2xl sm:text-3xl lg:text-4xl font-bold text-green-900">
                  <h2>Edit a Tropical Plant</h2>
              </div>
              <form method="POST"
                    action=""
                    class="flex items-center justify-center flex-col gap-4 w-full my-7">
                  {% csrf_token %}
                  <input type="hidden" name="remember" value="true">
                  <div class="w-full flex flex-col gap-2">
                      {% for field in form %}
                          <div class="flex flex-col">
                              <label for="username" class="font-medium">{{ field.label }}</label>
                              {{ field }}
                          </div>
                      {% endfor %}
                  </div>
                  <div class="w-full">
                      <input class="w-full bg-green-700 p-2 rounded-md text-white hover:bg-green-800 font-medium tracking-wide cursor-pointer !border-0"
                             type="submit"
                             value="Edit Tropical Plant!" />
                  </div>
              </form>
          </div>
      </section>
  {% endblock %}
  ```

  Setelah itu, menambahkan 2 path baru di file `urls.py` untuk kedua fungsi edit dan delete yang terdapat pada `views.py`

  ```python
  urlpatterns = [
      path(
          "edit-tropical-plant/<uuid:id>", edit_tropical_plant, name="edit_tropical_plant"
      ),
      path(
          "delete-tropical-plant/<uuid:id>", delete_tropical_plant, name="delete_tropical_plant",
      )
  ]
  ```

  Terakhir, menambahkan akses terhadap kedua fungsi tersebut kepada pengguna menggunakan link di halaman utama:

  ```htmldjango
  <a href="{% url 'main:edit_tropical_plant' plant.pk %}"
     class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg"
           class="h-6 w-6 sm:h-8 sm:w-8"
           viewBox="0 0 20 20"
           fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
  </a>
  <a href="{% url 'main:delete_tropical_plant' plant.pk %}"
     class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg"
           class="h-6 w-6 sm:h-8 sm:w-8"
           viewBox="0 0 20 20"
           fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
  </a>
  ```

- [x] Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

  Kustomisasi desain dilakukan menggunakan framework Tailwind CSS agar development berjalan lebih cepat dan tanpa adanya kerumitan mengatur class CSS.
  Untuk memulai, ditambahkan terlebih dahulu meta tag dengan `name="viewport"` agar perilaku website di browser mobile sesuai dengan harapan

  ```html
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  ```

  Kemudian opsi yang digunakan untuk menambahkan Tailwind ke dalam proyek adalah dengan menggunakan CDN (Content Delivery Network). Hal ini dapat dilakukan dengan menambahkan tag script pada bagian head seperti berikut:

  ```htmldjango
  {% block meta %}
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  {% endblock meta %}
  <script src="https://cdn.tailwindcss.com"></script>
  ```

  Setelah itu, Tailwind sudah dapat digunakan di aplikasi.

  Kemudian untuk menambahkan vanilla CSS ke dalam proyek, pertama dilakukan konfigurasi terhadap static files dalam proyek agar file static seperti file CSS dapat digunakan oleh aplikasi. Di file `settings.py` ditambahkan middleware baru untuk memudahkan konfigurasi file statis saat dalam production environment:

  ```python
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
      ...
  ]
  ```

  Setelah itu, dilakukan konfigurasi terhadap variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL`:

  ```python
  ...
  STATIC_URL = '/static/'
  if DEBUG:
      STATICFILES_DIRS = [
          BASE_DIR / 'static' # merujuk ke /static root project pada mode development
      ]
  else:
      STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
  ...
  ```

  Setelah mengonfigurasi direktori file statis, dibuat direktori baru di folder root projek yaitu `static/css` dan ditambahkan file `global.css`.

  Kemudian file ini dapat diakses oleh projek dengan menambahkan tag link di dalam head HTML:

  ```html
  {% load static %}
  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
      <script src="https://cdn.tailwindcss.com"></script>
      <link rel="stylesheet" href="{% static 'css/global.css' %}" />
    </head>
    <body>
      {% block content %} {% endblock content %}
    </body>
  </html>
  ```

  Terakhir, tambahkan style sesuai dengan kebutuhan pada file `global.css` untuk memberikan styling kepada elemen-elemen di dalam aplikasi.

</details>

---

### Jawaban Tugas :four:

<details>
    <summary>Lihat disini</summary>

##### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

Perbedaan antara `HttpResponseRedirect()` dan `redirect()` adalah bahwa `HttpResponseRedirect()` merupakan response berbentuk Class dan dapat dimodifikasi sesuai kebutuhan agar aplikasi dapat mengembalikan response dengan fungsi tertentu.

`redirect()` itu sendiri didesain untuk mengembalikan sebuah `HttpResponseRedirect()`, tetapi dengan menggunakan pemanggilan fungsi `redirect()`, navigasi terhadap suatu link dapat dilakukan dengan lebih fleksibel, seperti melalui string URL, nama sebuah view, atau objek model.

##### 2. Jelaskan cara kerja penghubungan model Product dengan User!

Penghubungan model Product (dalam aplikasi Plantify adalah `TropicalPlant`) dengan User dilakukan dengan menambahkan field baru pada model Product tersebut yang merepresentasikan hubungan dengan seorang User.

Dengan menghubungkan sebuah User dengan Product, telah dibuat jenis relasi yaitu many-to-one relationship yang berarti seorang User dapat memiliki banyak Product.

##### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication dan Authorization adalah dua konsep yang berbeda tetapi sering dianggap sama oleh banyak programmer.

Authentication merupakan proses untuk memperjelas peran suatu pengguna terhadap aplikasi yang sedang digunakan. Dalam kasus ini, aplikasi ingin mengetahui siapa pengguna yang sedang mengaksesnya dan apa perannya di dalam aplikasi ini.

Authorization adalah proses dimana aplikasi menentukan peran apa yang dapat mengakses suatu sumber daya dalam aplikasi tersebut. Sebagai contoh, mungkin seorang dengan peran User tidak memiliki akses terhadap aksi administratif dari suatu aplikasi, sementara pengguna dengan peran Admin dapat mengaksesnya.

##### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan membuat sebuah session storage pada server yang menyimpan seluruh user yang telah login kepada aplikasi tersebut. Django kemudian mengirimkan ID dari session tersebut kepada user yang login tersebut. Perlu diperhatikan bahwa session ID bersifat unik dan berfungsi untuk mengidentifikasi user pada aplikasi Django tersebut.

Session ID yang dikirimkan oleh server kemudian disimpan oleh browser yang menerimanya di dalam penyimpanan bernama cookies. Sang user kemudian dapat mencantumkan session ID ini di request-request yang dikirimkan kepada aplikasi sebagai bentuk authentication dan authorization terhadap peran user dalam aplikasi tersebut.

Selain untuk menyimpan session ID, cookies biasanya digunakan untuk menyimpan preferensi dari pengguna aplikasi agar saat user kembali ke web tersebut setelah waktu yang lama, aplikasi masih dapat mengingat preferensi user tersebut sejak terakhir kali menggunakannya.

##### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

  1. Pengimplementasian fungsi registrasi, login, dan logout dimulai dengan menambahkan ketiga fungsionalitas tersebut di file `views.py`:

  ```python
  def register(request):
      form = UserCreationForm()

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, "Your account has successfully been created!")
              return redirect("main:login")

      context = {"form": form}
      return render(request, "register.html", context)


  def login_user(request):
      if request.method == "POST":
          form = AuthenticationForm(data=request.POST)

          if form.is_valid():
              user = form.get_user()
              login(request, user)
              response = HttpResponseRedirect(reverse("main:show_main"))
              response.set_cookie("last_login", str(datetime.datetime.now()))
              return response

      else:
          form = AuthenticationForm(request)
      context = {"form": form}
      return render(request, "login.html", context)


  def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse("main:login"))
      response.delete_cookie("last_login")
  ```

````

```

```

2. Membuat 2 template HTML baru yaitu `register.html` dan `login.html` yang berfungsi sebagai form register dan login untuk aplikasi

3. Menambahkan fungsionalitas dari `views.py` ke file `urls.py` untuk meng-ekspose fungsi-fungsi tersebut.

```python
urlpatterns = [
    ...
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
```

4. Terakhir, menambahkan tag baru di file `main.html` yang berfungsi sebagai tombol logout dari halaman utama:

```html
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
      Pembuatan akun dilakukan dengan me-register ke aplikasi dengan 2 identitas berbeda, kemudian menambahkan tiga dummy data untuk setiap akun tersebut.
- [x] Menghubungkan model Product dengan User.

  Menghubungkan model Product (dalam aplikasi Plantify adalah model TropicalPlant) dilakukan dengan menambahkan field baru di model tersebut:

  ```python
  class TropicalPlant(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
      weight = models.FloatField()
      created_at = models.DateTimeField(auto_now_add=True)
  ```

  Model di atas ditambahkan field baru yaitu `user` yang mereferensikan terhadap seorang User dengan bantuan `ForeignKey()`. Dengan ini, telah terbuat relasi one-to-many yaitu setiap user dapat memiliki relasi dengan banyak instansi dari model ini.
  `on_delete=models.CASCADE` menyatakan bahwa jika suatu User di-delete, maka seluruh instansi dari TropicalPlant yang memiliki relasi terhadap User tersebut akan dihapus.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

  Informasi tentang pengguna yang sedang login dapat diakses melalui request yang dikirimkan kepada aplikasi. Seperti contoh, dapat dilihat pada fungsi `show_main()` bahwa:

  ```python
  def show_main(request):
      tropical_plant_entries = TropicalPlant.objects.filter(user=request.user)
      context = {
          "app_name": "Plantify Shop",
          "name": request.user.username,
          "class": "PBP-D",
          "npm": "2306215160",
          "tropical_plants": tropical_plant_entries,
          "last_login": request.COOKIES["last_login"],
      }

      return render(request, "main.html", context)
  ```

  Data `name` dapat diambil dari objek user yang mengirim request tersebut, sedangkan `last_login` dapat diakses berdasarkan cookies yang telah tersimpan di browser pengguna dan dicantumkan bersama dengan request yang dikirim oleh user.

</details>

---

### Jawaban Tugas :three:

<details>
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
````
