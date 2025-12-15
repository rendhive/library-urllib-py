import urllib.request

url = 'http://www.example.com'
filename = 'output.html'

with urllib.request.urlopen(url) as response:
    with open(filename, 'wb') as f:
        f.write(response.read())
print(f"Data disimpan di {filename}.")
# Fungsi: Mengambil data dari URL dan menyimpannya ke dalam file.
# Kondisi: Ketika Anda perlu menyimpan konten web ke file lokal untuk penggunaan selanjutnya.
