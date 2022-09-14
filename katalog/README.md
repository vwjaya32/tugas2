Nama = Vinsen Wijaya  
NPM  = 2106637776  
[Link Heroku](https://pbp-tugas2-vinsen.herokuapp.com/katalog/)

---

# BAGAN
![Bagan MVT](https://github.com/vwjaya32/tugas2/blob/main/baganMVT.png)

# VIRTUAL ENVIRONMENT
_Web_ berbasis Django tetap dapat dibuat tanpa harus menggunakan _virtual environment_. Penggunaan _virtual environment_ dianjurkan karena kebutuhan modul-modul pada sebuah projek berbeda dengan projek yang lainnya, termasuk kebutuhan versi suatu modul. Perbedaan ini memungkinkan terjadinya _error_ apabila seseorang ingin menjalankan dua program yang membutuhkan sebuah modul dengan versi yang berbeda (salah satu program membutuhkan versi yang lebih lama). Dengan menggunakan _virtual environment_ kebutuhan modul (serta versinya) dapat diatur sesuai dengan kebutuhan projek dan instalasi modul yang dilakukan tidak akan berdampak ke dalam sistem secara global.   [Referensi](https://youtu.be/mOwgdXT6WMM).

# CARA IMPLEMENTASI  
Implementasi yang saya lakukan dalam tugas 2 mengacu pada langkah-langkah tutorial 0 dan 1.

**Langkah 1**  
>Dengan meniru fungsi serupa yang telah dibuat pada _tutorial_ 1, saya membuat fungsi baru bernama ```show_katalog```. 

**Langkah 2**  
>Pembuatan _routing_ dilakukan pada ```urls.py``` dalam folder ```katalog```. Selain itu, daftarkan juga aplikasi katalog ke dalam fungsi ```urlpatterns``` pada ```urls.py``` yang berada di dalam ```project_django```.

**Langkah 3**  
>Pertama, saya menambahkan variabel ```context``` seperti pada tutorial 1 dan juga menambahkan ```context``` pada parameter fungsi ```render```. Kedua, melakukan perubahan pada file ```katalog.html```, dengan menambahkan iterasi terhadap variabel  ```list_item```.

**Langkah 4**  
>Dikarenakan file ```dpl.yml``` dan ```Procfile``` telah dibuat, maka yang saya lakukan pertama adalah membuat _app_ baru di Heroku. Setelah itu mengonfigurasi _repository_ GitHub dengan menambahkan variabel _repository_ secret baru (API _Key_ dan nama _app_).  

