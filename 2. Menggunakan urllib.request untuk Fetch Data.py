import urllib.request

response = urllib.request.urlopen('http://www.example.com')
data = response.read()
print("Data dari example.com:", data[:50])  # Menampilkan 50 karakter pertama
# Fungsi: Mengambil data dari URL menggunakan urllib.request.
# Kondisi: Ketika Anda ingin mengakses konten dari halaman web.
