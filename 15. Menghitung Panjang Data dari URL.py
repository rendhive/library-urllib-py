import urllib.request

url = 'http://www.example.com'

with urllib.request.urlopen(url) as response:
    data = response.read()
    print("Panjang data:", len(data))
# Fungsi: Mengambil dan menghitung panjang data dari halaman web.
# Kondisi: Ketika Anda ingin mengetahui ukuran konten yang diambil.
