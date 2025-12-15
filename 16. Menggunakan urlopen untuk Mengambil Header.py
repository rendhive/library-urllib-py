import urllib.request

url = 'http://www.example.com'
with urllib.request.urlopen(url) as response:
    print("Headers:", response.getheaders())
# Fungsi: Mengambil header dari respons permintaan URL.
# Kondisi: Ketika Anda perlu menganalisis header respons dari server.
