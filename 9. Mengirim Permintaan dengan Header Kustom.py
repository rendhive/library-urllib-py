import urllib.request

url = 'http://www.example.com/'
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
print("Page title:", response.url)
# Fungsi: Mengirim permintaan ke server dengan menggunakan header kustom.
# Kondisi: Ketika Anda perlu mengidentifikasi diri dalam permintaan (mis., menggunakan user-agent).
