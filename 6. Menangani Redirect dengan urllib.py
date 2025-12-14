import urllib.request

response = urllib.request.urlopen('http://python.org/')
print("Page title:", response.geturl())  # Menampilkan URL akhir setelah redirect
# Fungsi: Menggunakan urllib untuk mengikuti redirect otomatis.
# Kondisi: Ketika Anda ingin mendapatkan halaman akhir setelah pelacakan redirect.
