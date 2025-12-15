import urllib.request

url = 'https://www.example.com/image.png'
filename = 'image.png'

urllib.request.urlretrieve(url, filename)
print(f"{filename} berhasil diunduh.")
# Fungsi: Mengunduh file dari URL dan menyimpannya ke direktori lokal.
# Kondisi: Ketika Anda memiliki URL file dan ingin menyimpannya secara langsung.
