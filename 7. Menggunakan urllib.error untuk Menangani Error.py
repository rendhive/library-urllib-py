import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.nonexistentwebsite.xyz')
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
except urllib.error.URLError as e:
    print("Failed to reach a server:", e.reason)
# Fungsi: Menangani kesalahan ketika mengambil data dari URL.
# Kondisi: Ketika Anda ingin menangani error yang muncul saat mengakses URL yang mungkin tidak valid.
