import urllib.request

url = 'http://www.example.com/image.png'
filename = 'downloaded_image.png'
urllib.request.urlretrieve(url, filename)
print(f"File telah diunduh dan disimpan sebagai {filename}.")
# Fungsi: Mengunduh file dari URL dan menyimpannya ke disk.
# Kondisi: Ketika Anda perlu menyimpan file dari internet ke sistem lokal.
