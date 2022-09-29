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

# Alur Data

# Implementasi
