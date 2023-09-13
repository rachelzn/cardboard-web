# pool_inventory
Cue Inventory App for Platform-Based Programming Assignment

Langkah-langkah dalam mengimplementasikan tugas ini:

1. Membuat Proyek Django Baru
   Untuk membuat proyek Django baru, saya pertama-tama membuat direktori baru di desktop saya, dengan nama 'pool_inventory.'
   Selanjutnya, saya membuka terminal di dalam direktori tersebut dan membuat virtual environment dengan menjalankan perintah "python -m venv env."
   Setelah itu, saya mengaktifkan virtual environment dengan perintah "source env/bin/activate" dan membuat file 'requirements.txt' di dalam direktori tersebut. Saya menginstal dependensi yang diperlukan dengan menggunakan "pip install -r requirements.txt."
   Terakhir, saya menggunakan command "django-admin startproject inventory_list ." untuk membuat proyek Django. Setelah membuatnya, saya membuka folder tersebut di Visual Studio Code dan mengedit 'ALLOWED_HOSTS' di 'settings.py' menjadi "ALLOWED_HOSTS = ["*"]."
   Kemudian, saya menonaktifkan virtual environment. Setelah menyelesaikan langkah-langkah ini, saya membuat file '.gitignore' di dalam direktori 'pool_inventory'.

2. Membuat Aplikasi dengan Nama 'main' di dalam Proyek
    Saya membuat aplikasi 'main' dengan menjalankan command "python manage.py startapp main" dan mendaftarkannya dengan menambahkan 'main' ke daftar 'INSTALLED_APPS' di file 'settings.py' yang terletak di direktori proyek 'pool_inventory.'

3. Membuat Konfigurasi Routing URL untuk Mengakses Aplikasi 'main'

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

4. Selanjutnya, saya membuat model di dalam aplikasi 'main' dengan nama 'Item' dan atribut-atribut wajib berikut: 
    
    Pertama, saya menambahkan kode berikut ke dalam file 'models.py' di dalam direktori aplikasi 'main':

    ```
    from django.db import models

    class Item(models.Model):
    #...
    ```

    Dan saya menambahkan atribut-atribut dengan tipe data masing-masing.
    
    Selanjutnya, saya membuat migrasi model dengan menjalankan perintah-perintah berikut di terminal

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    Perintah-perintah ini menghasilkan dan menerapkan migrasi untuk model 'Item' ke basis data lokal.

5. Buat sebuah fungsi di views.py yang mengembalikan template HTML yang berisi nama aplikasi Anda, nama Anda, dan kelas Anda.
   Pertama, saya membuat file HTML dalam direktori baru yang disebut "templates" di dalam aplikasi 'main'. Selanjutnya, saya menghubungkan
   views ke template dengan menambahkan "from django.shortcuts import render" di file views.py yang terletak di dalam aplikasi 'main' dan menambahkan kode berikut:
   ```
    def show_main(request):
    context = {
        'Name': 'Beginner Cue',
        'Force': 'very low',
        'Aim': 'very low',
        'Spin': 'very low',
        'Time': 'very low',
    }

    return render(request, 'main.html', context)
    ```

   Kemudian saya memodifikasi file main.html sebagai sebagai berikut:
   ```
   <h1> Welcome to POOL INVENTORY </h1>
   <h2> Cue Collection </h2>

   <h5>Name: </h5>
   <p>Beginner Cue</p>
   <h5>Force: </h5>
   <p>{{ Force }}</p> 
   <h5>Aim: </h5>
   <p>{{ Aim }}</p> 
   <h5>Spin: </h5>
   <p>{{ Spin }}</p> 
   <h5>Time: </h5>
   <p>{{ Time }}</p>
   ```
6. Buatlah routing di urls.py untuk menghubungkan fungsi di views.py ke URL.
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

     ```
7. Selanjutnya, saya melakukan deploy aplikasi ke Adaptable agar dapat diakses melalui internet.

  Sebelum melakukan deploy, saya telah membuat repositori baru di GitHub dengan nama "pool_inventory" dan melakukan push "pool_inventory" dari direktori 
  lokal saya ke repositori tersebut. Karena saya sudah menghubungkan Adaptable.io dengan GitHub, saya memilih repositori "pool_inventory" sebagai dasar 
  untuk aplikasi yang akan di-deploy dan memilih branch master. Untuk template deployment, saya memilih Python App Template, dan untuk jenis database, 
  saya memilih PostgreSQL. Selanjutnya, saya menyesuaikan versi Python dan memasukkan perintah berikut di bagian start command: 
  "python manage.py migrate && gunicorn shopping_list.wsgi". 
  Saya juga memasukkan nama aplikasi dan akhirnya melakukan deploy aplikasi tersebut.

8. Terakhir, saya membuat file README.md. Saya telah membuat README.md sebelum melakukan push "pool_inventory" ke GitHub. Saya membuatnya menggunakan
   editor teks dan meletakkannya di dalam direktori yang sama dengan "pool_inventory."













   
