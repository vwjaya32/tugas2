Nama = Vinsen Wijaya  
NPM  = 2106637776  
[Link Heroku](https://pbp-tugas2-vinsen.herokuapp.com/mywatchlist/)

---

# Perbedaan JSON, XML, dan HTML

### JSON (JavaScript Object Notation)
_File extension_ : `.json`  
  
`1.` Digunakan untuk menyimpan dan mengirim data.  
`2.` _Object_ JSON memiliki beberapa _type_.  
`3.` Data disimpan dalam bentuk _key_ dan _value_.  
`4.` Dapat merepresentasikan data sebagai _Array_.  
`5.` Memiliki _syntax_ yang singkat ketimbang HTML dan XML.  
`6.` Lebih cepat dibanding XML apabila dijalankan pada AJAX.  
`7.` Ukuran data lebih kecil dari XML.  

### XML (Extensible Markup Language)  
_File extension_ : `.xml`  
  
`1.` Digunakan dalam pengiriman data.  
`2.` Data XML tidak memiliki _type_.  
`3.` Menggunakan _tag_ untuk mendeskripsikan data.    
`4.` Tidak memiliki konsep _Array_.  
`5.` _Tag_ dalam _syntax_ belum terdefinisi. Definisi tag dilakukan oleh _programmer_.      
`6.` Dapat menyimpan _whitespace_.  
`7.` Ukuran dokumen relatif lebih besar dari HTML dan JSON.  
`8.` Memerlukan DOM (_Document Object Model_) untuk _parsing_ kode Javascript.  

### HTML (Hyper Text Markup Language)  
_File extension_ : `.html` 
  
`1.` Digunakan untuk menampilkan data.  
`2.` Menggunakan _tag_ untuk menampilkan data.  
`3.` _Tag_ dalam _syntax_ telah didefinisikan.  
`4.` Tidak dapat menyimpan _whitespace_.  
`5.` Ukuran dokumen relatif kecil dari XML.  
`6.` Tidak memerlukan aplikasi lain untuk _parsing_ kode Javascript.  
  
  
# Pentingnya _Data Delivery_  
# Langkah Implementasi

- [x] Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu  
1. Buka direktori tugas 2  
2. Masuk ke dalam Virtual Environment  
3. Jalankan 
```python
py manage.py startapp mywatchlist`
```  
<br/>
      
- [x] Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist    
1. Menambahkan `'mywatchlist'` dalam `INSTALLED_APPS` pada `settings.py` dari folder `project_django`  
2. Masih dalam folder `project_django`, menambahkan potongan kode berikut ke dalam `urls.py`  
```python
   path('mywatchlist/', include('mywatchlist.urls'))
```       
<br />
      
- [x] Membuat sebuah model MyWatchList yang memiliki atribut yang bersesuaian.
Menambahkan model `MyWatchList` di dalam `models.py`dengan isi sebagai berikut:
```python
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
```  
<br />

- [x] Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
1. Menambahkan _folder_ `fixtures`
2. Menambahkan _file_ `initial_mywatchlist_data.json` di dalam `fixtures`. Contoh 1 data:
```json
[
    {
        "model": "mywatchlist.MyWatchList",
        "pk": 1,
        "fields": {
            "watched"     : true,
            "title"       : "Avengers: Endgame",
            "rating"      : 4.2,
            "release_date": "April 24, 2019",
            "review"      : "This film is an emotional rollercoaster with some of the coolest superhero plot lines ever drawn up. It's straight up the most epic Marvel film that will probably ever be created."
        }
    },
    ...
 ]
 ```  
<br />

- [x] Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
  - [x] HTML
        Membuat _function_ `show_html` pada `views.py` dengan isi sebagai berikut:
  ```python
  def show_html(request):
    not_watched_count = MyWatchList.objects.filter(watched=False).count()
    watched_count     = MyWatchList.objects.filter(watched=True).count()
    half_watched      = True if watched_count >= not_watched_count else False
    
    data = MyWatchList.objects.all
    context = {
        'half_watched'  : half_watched,
        'list_film': data,
    }
    return render (request, "mywatchlist.html", context)
  ```
  <br />
  
  - [x] XML
        Membuat _function_ `show_xml` pada `views.py` dengan isi sebagai berikut:
  ```python
  def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  ```
  <br />
  
  - [x] JSON
        Membuat _function_ `show_json` pada `views.py` dengan isi sebagai berikut:
  ```python
  def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
  <br />
  
- [x] Membuat routing sehingga data di atas dapat diakses melalui URL
      Menambahkan beberapa baris kode pada variabel `urlpatterns` dalam `urls.py` di _folder_ `mywatchlist`
```python
urlpatterns = [
    ...
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```
<br />

- [x] Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.  
      Git add, commit, dan push dari repositori lokal. Dikarenakan saya menggunakan folder tugas 2 yang sebelumnya telah menjalankan prosedur _deployment_, maka hasil pekerjaan dapat langsung dilihat dengan [_link_ Heroku yang sama](https://pbp-tugas2-vinsen.herokuapp.com/mywatchlist/).
<br />
