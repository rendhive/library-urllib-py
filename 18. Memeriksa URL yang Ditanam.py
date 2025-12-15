import urllib.request

url = 'http://www.example.com'
req = urllib.request.Request(url)
try:
    response = urllib.request.urlopen(req)
    print("URL checked successfully.")
except Exception as e:
    print("Error:", e)
# Fungsi: Memeriksa status URL sebelum mengambil data sebenarnya.
# Kondisi: Ketika Anda ingin memastikan bahwa URL valid dan dapat diakses.
