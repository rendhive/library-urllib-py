import urllib.request

url = 'http://www.example.com'
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html.decode('utf-8'))  # Menampilkan konten HTML
# Fungsi: Mengambil konten dari URL dan menampilkan sebagai teks.
# Kondisi: Ketika Anda ingin menampilkan data HTML dari sebuah situs web.
