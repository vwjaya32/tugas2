## Synchronous vs Asynchronous Programming
Synchronous programming: pendekatan dalam pemrograman di mana program yang dihasilkan akan mengerjakan tugas yang diberikan secara bertahap (_sequential order_) sehingga tugas yang baru diinput baru akan dikerjakan setelah tugas sebelumnya selesai.

Asynchronous programming: pendekatan dalam pemrograman di mana program yang dihasilkan akan menjalankan perintah secara bersamaan, bukan dalam urutan sekuensial.

| Perbedaan    | Asynchronous   | Synchronous     |
|--------------|----------------|-----------------|
| Kompleksitas | Lebih kompleks | Lebih sederhana |
| Loading time | Lebih cepat    | Lebih lamban    |

## Event-Driven Programming
Merupakan suatu pendekatan dalam pemrograman di mana program akan merespon terhadap suatu peristiwa. Penerapan Event Driven Programming dalam tugas kali ini terdapat pada implementasi tombol `add_task` di mana tombol ini akan menjalankan method POST menggunakan AJAX. 

## Asynchronous Programming pada AJAX
AJAX memungkinkan web untuk meng-update kontennya secara asinkronus, itu berarti web tidak perlu di-reload untuk mengubah sedikit informasi pada konten.

## Langkah Implementasi
1. Membuat view baru yaitu show_json dan melakukan setting path
2. Implementasi Modal menggunakan Bootstrap
3. Implementasi function AJAX (loadCard dan makeCard untuk menampilkan kartu serta mengimplementasikan event-driven programming pada button dalam modal) 
4. Implementasi routing
5. Implementasi tutup modal dengan `$("#add-task-modal").modal("hide")`
6. 
