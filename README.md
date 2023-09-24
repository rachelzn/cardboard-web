# Rachel's Pool Cue Inventory
Inventory App for Platform-Based Programming 2023/2024 Assignment. Managed by Rachel Heningtyas Zanetta Erari - 2206081944.

## Tugas 2
### 1. Langkah-langkah Implementasi Tugas 2

<details>
<summary>Membuat Proyek Django Baru</summary>
Untuk membuat proyek Django baru, saya pertama-tama membuat direktori baru di desktop saya, dengan nama 'pool_inventory.'
Selanjutnya, saya membuka terminal di dalam direktori tersebut dan membuat virtual environment dengan menjalankan perintah "python -m venv env."
Setelah itu, saya mengaktifkan virtual environment dengan perintah "source env/bin/activate" dan membuat file 'requirements.txt' di dalam direktori tersebut.      Saya menginstal dependensi yang diperlukan dengan menggunakan
```
pip install -r requirements.txt.
```
Terakhir, saya menggunakan command
```
django-admin startproject pool_inventory.
```
untuk membuat proyek Django. Setelah membuatnya, saya membuka folder tersebut di Visual Studio Code dan mengedit 'ALLOWED_HOSTS' di 'settings.py' menjadi          ALLOWED_HOSTS = ["*"]. Kemudian, saya menonaktifkan virtual environment. Setelah menyelesaikan langkah-langkah ini, saya membuat file '.gitignore' di dalam direktori 'pool_inventory'.
</details>
<details>
<summary>Membuat Aplikasi dengan Nama 'main' di dalam Proyek</summary>
Saya membuat aplikasi 'main' dengan menjalankan command "python manage.py startapp main" dan mendaftarkannya dengan menambahkan 'main' ke daftar 'INSTALLED_APPS' di file 'settings.py' yang terletak di direktori proyek 'pool_inventory.'
</details>
<details>
<summary>Membuat Konfigurasi Routing URL untuk Mengakses Aplikasi 'main'</details>
Pertama-tama, saya menambahkan kode berikut ke file 'urls.py' di dalam direktori 'inventory_list':
```
from django.urls import path, include
```
Dan kemudian, saya menambahkan baris berikut ke dalam daftar 'urlpatterns':
```
path('', include('main.urls')),
```
Selanjutnya, saya mengonfigurasi routing URL untuk aplikasi 'main'. Pertama-tama, saya membuat file 'urls.py' di dalam aplikasi 'main'
dan mengimpor "from main.views import show_main" serta menambahkan "path('', show_main, name='show_main')" dalam pola URL-nya. Dengan langkah-langkah ini,
saya berhasil membuat aplikasi 'main' di proyek Django saya dan mengonfigurasi routing URL untuk mengaksesnya.
</details>
<details>
<summary>Membuat model di dalam aplikasi 'main'</summary>
Pertama, saya menambahkan kode berikut ke dalam file 'models.py' di dalam direktori aplikasi 'main':
```
from django.db import models
class Item(models.Model):
    #...
```
Dan saya menambahkan atribut-atribut dengan tipe data masing-masing.
</details>
<details>
<summary>Migrasi model dengan menjalankan perintah-perintah berikut di terminal</summary>
```
python manage.py makemigrations
python manage.py migrate
```
Perintah-perintah di atas menghasilkan dan menerapkan migrasi untuk model 'Item' ke basis data lokal.
</details>
<details>
<summary>Membuat fungsi di views.py yang mengembalikan template HTML yang berisi nama aplikasi, nama, dan kelas</summary>
Pertama, saya membuat file HTML dalam direktori baru yang disebut "templates" di dalam aplikasi 'main'. Selanjutnya, saya menghubungkan views ke template dengan menambahkan "from django.shortcuts import render" di file views.py yang terletak di dalam aplikasi 'main' dan menambahkan kode berikut:
```
def show_main(request):
    context = {
        'app_name': 'Rachel\'s Cue Collection',
        'name': 'Rachel Heningtyas Zanetta Erari',
        'class': 'PBP C',
    }

    return render(request, 'main.html', context)
```
Kemudian saya memodifikasi file main.html sebagai sebagai berikut:
```
    <h1>{{ app_name }}</h1>
    <h2>Cue Collection by Rachel Heningtyas Zanetta Erari</h2>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>
``
</details>
<detail>
<summary>Membuat routing di urls.py untuk menghubungkan fungsi di views.py ke URL</summary>
    Saya menambahkan kode berikut ke dalam file urls.py di dalam aplikasi 'main':
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'
    urlpatterns = [
    path('', show_main, name='show_main'),
    ]
    ```
    Selanjutnya, saya mendefinisikan pola URL di dalam file urls.py di dalam direktori proyek 'pool_inventory' menggunakan path() seperti berikut:
     ```
     path('main/', include('main.urls')),

     ``
</details>
<details>
<summary>Deploy aplikasi ke Adaptable</summary>
Sebelum melakukan deploy, saya telah membuat repositori baru di GitHub dengan nama "pool_inventory" dan melakukan push "pool_inventory" dari direktori lokal saya ke repositori tersebut. Karena saya sudah menghubungkan Adaptable.io dengan GitHub, saya memilih repositori "pool_inventory" sebagai dasar 
untuk aplikasi yang akan di-deploy dan memilih branch main. 
Untuk template deployment, saya memilih Python App Template, dan untuk jenis database, saya memilih PostgreSQL. Selanjutnya, saya menyesuaikan versi Python dan memasukkan perintah berikut di bagian start command: "python manage.py migrate && gunicorn shopping_list.wsgi". 
Saya juga memasukkan nama aplikasi dan akhirnya melakukan deploy aplikasi tersebut.
</details>
<details>
<summary>Membuat file README.md</summary>
Terakhir saya membuat README.md sebelum melakukan push "pool_inventory" ke GitHub. 
Saya membuatnya menggunakan editor teks dan meletakkannya di dalam direktori yang sama dengan "pool_inventory."
</details>

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="774" alt="Screenshot 2023-09-13 at 11 52 25" src="https://github.com/rachelzn/pool_inventory/assets/92985397/c996b4cf-cf1d-40a2-9465-437c84f26772">
Reference: Intellipaat

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita menggunakan virtual environment karena virtual environment mengisolasi dan mengelola dependensi yang spesifik untuk proyek kita, memastikan agar dependensi tersebut tidak bersinggungan dengan proyek lain. Membangun aplikasi web Django tanpa virtual environment memang memungkinkan, tetapi tidak disarankan karena dapat menyebabkan konflik dependensi.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC, MVT, dan MVVM adalah tiga pola desain yang populer dalam pengembangan perangkat lunak.
#### MVC (Model-View-Controller)
 sering ditemukan dalam aplikasi web dan desktop tradisional. Model: menyimpan data aplikasi. View: menampilkan data. Controller: mengelola komunikasi antara Model dan View
### MVT (Model-View-Template) 
biasanya digunakan dalam kerangka kerja web seperti Django. Model: menyimpan data aplikasi. View: menampilkan data. Template: mendefinisikan bagaimana data ditampilkan (misalnya, HTML).
#### MVVM (Model-View-ViewModel) 
sering ditemukan dalam aplikasi web modern. Model: menyimpan data aplikasi. View: menampilkan data. ViewModel berfungsi sebagai penghubung antara model dan tampilan serta mengatasi logika antarmuka pengguna

## Tugas 3
### 1. Langkah-Langkah Implementasi Tugas 3
<details>
<summary>Membuat input form</summary>
Pertama-tama, saya membuat folder bernama 'templates' di dalam direktori root dan merancang template base.html sebagai struktur dasar situs web saya. Selanjutnya, saya melakukan beberapa perubahan pada berkas settings.py yang terletak di dalam direktori 'inventory_list', dengan menambahkan baris: 'DIRS': [BASE_DIR / 'templates'],. Setelah itu, saya melakukan penyesuaian pada berkas main.html untuk menggunakan base.html sebagai templatenya.

Selanjutnya, saya membuat forms.py di dalam folder 'main' dan menambahkan kode berikut:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
Saya juga menambahkan impor tambahan di dalam berkas views.py yang terletak di dalam folder 'main'. Setelah itu, saya membuat sebuah fungsi baru:
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
Setelah itu, saya menambahkan dua baris berikut di dalam fungsi show_main:
```
products = Product.objects.all()
'products': products
```
dan jufa mengimpor fungsi create_product di dalam berkas urls.py yang terletak di dalam folder utama:
```
path('create-product', create_product, name='create_product'),
```
Terakhir, saya membuat file baru bernama create_product.html. File ini adalah template halaman web yang dirancang untuk menambahkan produk baru. Template ini meng-extend template lain yang disebut base.html. Kemudiab, saya menambahkan kode ke dalam main.html untuk menampilkan data produk dalam format tabel dan menambahkan tombol untuk mengarahkan ke halaman formulir.
</details>
<detail>
<summary>Menambahkan fungsi views untuk melihat objek dalam JSON & XML</summary>
Untuk langkah selanjutnya, saya menambahkan 5 tampilan untuk melihat objek yang ditambahkan dalam format HTML, XML, JSON, XML berdasarkan ID, dan JSON berdasarkan ID. Saya memulai dengan format XML. Saya mengimpor yang berikut ke dalam views.py di dalam folder 'main':
```
from django.http import HttpResponse
from django.core import serializers
```
Kemudian, saya membuat sebuah fungsi bernama show_xml yang membuat variabel untuk menyimpan semua objek 'Product' yang diambil:
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Selanjutnya, saya mengimpor fungsi show_xml ke dalam urls.py di dalam folder 'main' dan juga menambahkan jalur:
```
path('xml/', show_xml, name='show_xml'),
```
Hal yang sama saya lakukan untuk versi JSON. Saya mengikuti langkah yang sama di kedua berkas views.py dan urls.py. Namun, kali ini saya mengimplementasikannya dalam format JSON alih-alih XML.
</details>
<details>
<summary>Membuat routing URL untuk tiap views</summary>
Saya menambahkan dua fungsi berikut ke dalam views.py:
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Untuk menambahkan routing URL, saya mengimport fungsi-fungsi XML dan JSON yang telah saya buat ke urls.py:
```
from main.views import show_main, create_item, show_xml, show_json, show_json_by_id, show_xml_by_id
```
Kemudian, saya mengimpor fungsi-fungsi ini ke dalam urls.py di dalam folder 'main' dan menambahkan Path berikut:
```
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('xml/<int:id>/', show_xml_by_id, name="show_xml_by_id"),
    path('json/<int:id>/', show_json_by_id, name="show_json_by_id")
]
``
Dua path pertama berfungsi untuk menampilkan seluruh data pada database dalam format XML atau JSON, yang menggunakan fungsi show_xml dan show_json dari views. Dua path terakhir berfungsi untuk menampilkan data berdasarkan id yang di-input pada path dalam format XML atau JSON menggunakan fungsi show_xml_by_id dan fungsi show_json_by_id. Misalnya, untuk melihat data dengan id 1 dalam bentuk JSON, maka kita dapat membuka url http://localhost:8000/json/1, dan seterusnya.
</details>

### 2. Apa perbedaan antara form POST dan form GET dalam Django?
|kriteria           | POST                                                    | GET                                               |
|-------------------| --------------------------------------------------------| --------------------------------------------------|
|delivery           | Data dikirimkan secara background                       | Data dikirimkan melalui URL                       |
|visibility         |Tidak terlihat di URL                                    | Terlihat di URL dan di riwayat browser            |
|security           |Cocok untuk data sensitif, seperti username dan password | Cocok untuk data non-sensitif                     |
|batasan data length|Tidak ada batasan data length                            | Terbatas oleh URL length, memiliki batasan        |
|general use        |Formulir autentikasi, pengiriman data sensitif           | Permintaan pencarian, tautan, data non-sensitif   |

### 3. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
HTML digunakan untuk menampilkan data yang telah diproses dan berfokus pada tampilan dan presentasi konten. XML adalah bahasa markup dengan data yang terstruktur seperti pohon dari root, branch, hingga leaves, dan menggunakan tag. JSON digunakan untuk menyimpan dan mengirimkan data dengan menggunakan pasangan key-value. XML dan JSON keduanya sama-sama digunakan untuk menyimpan atau mengirimkan data, sedangkan HTML digunakan untuk menampilkan data yang telah diproses dan menekankan tampilan dan presentasi konten.

### 4. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON menyediakan kesederhanaan dan readability, baik bagi manusia maupun mesin. Strukturnya terdiri dari pasangan key-value dan array, sehingga lebih mudah dibaca (parse) dan ditulis ke file JSON. Kelebihan ini membuat JSON cocok untuk berbagai bahasa pemrograman dan sangat sesuai untuk aplikasi web, terutama yang menggunakan JavaScript.

### Mengakses URL melalui Postman
#### GET / (HTML)

![](https://cdn.discordapp.com/attachments/867838741099315210/1154058827470221403/Screenshot_2023-09-20_at_21.14.17.png)

#### GET /xml (XML)

![](https://cdn.discordapp.com/attachments/867838741099315210/1154058828002893855/Screenshot_2023-09-20_at_21.12.38.png)

#### GET /xml/1 (XML)

![](https://cdn.discordapp.com/attachments/867838741099315210/1154058826396479528/Screenshot_2023-09-20_at_21.13.10.png)

#### GET /json (JSON)

![](https://cdn.discordapp.com/attachments/867838741099315210/1154058826711048283/Screenshot_2023-09-20_at_21.13.19.png)

#### GET /json/1 (JSON)

![](https://cdn.discordapp.com/attachments/867838741099315210/1154058826992078998/Screenshot_2023-09-20_at_21.13.31.png)




   
