Nama = Vinsen Wijaya  
NPM  = 2106637776  
[Link Heroku](https://pbp-tugas2-vinsen.herokuapp.com/todolist/)

---

# Kegunaan `{% csrf_token %}`
Kode tersebut digunakan untuk membuat suatu token yang akan bertindak sebagai _user session id_. Untuk setiap pemanggilan method POST dari form, token akan diikutsertakan dan dicek oleh server. Apabila request diberikan dengan token yang berbeda dengan token csrf, request akan ditolak oleh server.
Hal ini bertujuan untuk melindungi web dari serangan CSRF (Cross-site Request Forgery).

### CSRF
Serangan web dengan cara mengelabui pengguna (misalnya dengan menekan suatu link) sehingga dapat melakukan request ke web yang telah menyimpan cookies login pengguna.

# Membuat `<form>` secara manual
1. Membuat tag `<form>` dab menspesifikasi `METHOD` yang akan dilakukan
2. Masukkan kode di dalam tag form `{% csrf_token %}`
3. Untuk menambahkan kotak yang akan diisi oleh user dapat menggunakan tag <input>
4. Untuk menambahkan teks di sebelah kotak dapat menggunakan tag <label>

# Alur Data
1. Setelah user mengisi form, user akan menekan tombol submit dan data akan divalidasi oleh server (misalnya validasi csrf token)
2. View akan membaca method yang didapat dari request
3. Data dari form kemudian akan dimasukkan ke dalam database
4. Kemudian views akan mengambil data-data yang sudah dimanipulasi untuk ditaruh pada sebuah variabel
5. Variabel tersebut akan dirender dan akan terlihat pada template

# Implementasi
- [x] Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya.

1. Buka direktori tugas 2
2. Jalankan Virtual Environment
3. Jalankan `py manage.py startapp todolist`
</br>

- [x] Menambahkan _path_ `todolist` sehingga pengguna dapat mengakses         http://localhost:8000/todolist.
1. pada folder project_django:
   a. tambahkan nama app dalam INSTALLED_APPS
   b. tambahkan path pada urls.py
2. pada folder todolist:
   a. tambahkan urls.py
   b. Dengan kode sebagai berikut
</br>

- [x]  Membuat sebuah model `Task` yang memiliki atribut sebagai berikut:

Menambahkan potongan kode pada models.py. Berikut isi dari models.py setelah dimanipulasi
```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user        = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=True)
    title       = models.CharField(max_length=255)
    description = models.TextField()
```
</br>

- [x] Mengimplementasikan form registrasi, _login_, dan _logout_ agar pengguna dapat menggunakan `todolist` dengan baik.
Membuat form registrasi, login, dan logout dengan bantuan dari tutorial 3
</br>

- [x] Membuat halaman utama `todolist` yang memuat _username_ pengguna, tombol `Tambah Task Baru`, tombol _logout_, serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_.

Menggunakan bantuan dari tutorial 3 untuk memodifikasi todolist.html. Berikut merupakan hasilnya:
```python
{% extends 'base.html' %}

{% block content %}  
<h1> TO DO LIST </h1>
<h3> Welcome, {{user}} </h3>

<button><a href="{% url 'todolist:new_task' %}">Tambah Task Baru</a></button>

<br> </br>
<table BORDER = "1">
    <tr>
      <th style="width:20%">Date</th>
      <th style="width:20%">Title</th>
      <th style="width:20%">Description</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for item in data_list %}
    <tr>
      <td style="text-align:center;
                 white-space:nowrap">{{item.date}}</td>
      <td style="text-align:center;
                 white-space:nowrap">{{item.title}}</td>
      <td style="text-align:center;
                 white-space:nowrap">{{item.description}}</td>
    </tr>
    {% endfor %}
  </table>
<br></br>
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
{% endblock content %}
```
</br>

- [x] Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan deskripsi _task_.
1. Membuat forms.py
2. Memanfaatkan Modelform untuk membuat class form baru

```python
from django import forms
from todolist.models import Task

class NewTaskForm(forms.ModelForm):
    class Meta:
        model  = Task
        fields = {"title", "description"}
```
3. Membuat halaman HTML baru
```
<h1> New Task </h1>

<form method="POST">
    {% csrf_token %}
    <label> Title: </label> 
    <input style= "font-family: 'Times New Roman'" type="text" name="title" />
    <br>
    
    <label> Description: </label> 
    <input style= "font-family: 'Times New Roman'" type="text" name="description" />
    <input type="submit" value="Submit">
</form>
```
</br>
    
- [x] Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL berikut:
    
Menambahkan semua path yang diperlukan pada urlspattern di urls.py dari todolist.
```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    
    # REGISTER
    path('register/', register, name='register'),
    # LOGIN
    path('login/', login_user, name='login'),
    # LOGOUT
    path('logout/', logout_user, name='logout'),
    # NEW TASK
    path('create-task/', new_task, name='new_task'),
]
```
</br>
    
- [x] Melakukan _deployment_ ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Git add, commit, push
2. Karena menggunakan app heroku yang sama jadi tidak perlu mengonfigurasi apapun
</br>

- [x] Membuat **dua** akun pengguna dan **tiga** _dummy data_ menggunakan model `Task` pada akun masing-masing di situs web Heroku.
1. Menambah 2 akun baru pada app Heroku
2. Memanfaatkan fitur Tambah Task Baru untuk menambahkan tiga dummy data  

---

# Tugas 5
## Internal vs External vs Inline  

| Perbedaan          | Internal                                                                                                     | External                                                                                                   | Inline                                                                                                                                    |
|--------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Definisi           | Memasukkan CSS dengan memasukkan tag <style> pada header                                                     | Memasukkan CSS dengan file terpisah berekstensi .css                                                       | Memasukkan CSS dengan mendefinisikan <style> langsung pada tag elemen HTML                                                                |
| Prioritas          | Kedua                                                                                                        | Ketiga                                                                                                     | Pertama                                                                                                                                   |
| Tag yang berkaitan | <style> pada setiap page HTML                                                                                | <link>                                                                                                     | <style> pada setiap tag HTML                                                                                                              |
| Manfaat            | - Tidak perlu upload File - Dapat melakukan perubahan pada 1 page yang tidak memengaruhi page lain           | - File HTML terlihat lebih rapi - Loading file lebih cepat - Dapat digunakan untuk beberapa page sekaligus | - Proses load website lebih cepat - Berguna untuk memperbaiki kode dengan cepat - Membantu apabila hanya 1 elemen saja yang ingin dilihat |
| Kekurangan         | Performa website lebih lamban dan tidak efisien apabila style  ingin diterapkan pada beberapa file sekaligus | Jika file CSS gagal diload, maka halaman website akan berantakan                                           | Tidak efisien                                                                                                                             |
   
## Tag HTML5
| TAG       | Penjelasan                                     |
|-----------|------------------------------------------------|
| <a>       | Mendefinisikan _hyperlink_                     |
| <body>    | Mendefinisikan badan dokumen                   |
| <br>      | Spasi baris                                    |
| <form>    | Mendefinisikan form                            |
| <picture> | Mendefinisikan container untuk beberapa gambar |
| <title>   | Mendefinisikan Judul dokumen                   |
| <video>   | Memasukkan video pada dokumen HTML             |
   
## CSS Selector
| CSS Selector | Penjelasan seleksi                                             |
|--------------|----------------------------------------------------------------|
| Element      | Menggunakan nama elemen (tag)                                  |
| ID           | Menggunakan id elemen                                          |
| Class        | Menggunakan atribut _class_                                    |
| Universal    | Menggunakan *                                                  |
| Group        | Menggunakan beberapa selector di atas (dipisahkan dengan koma) |
   
## LANGKAH-LANGKAH IMPLEMENTASI


