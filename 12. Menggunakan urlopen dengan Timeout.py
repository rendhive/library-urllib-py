import urllib.request

try:
    response = urllib.request.urlopen('http://www.example.com', timeout=1)
    print("Data fetched successfully.")
except Exception as e:
    print("Error:", e)
# Fungsi: Menyediakan timeout untuk permintaan URL.
# Kondisi: Ketika Anda ingin mencegah program terjebak karena permintaan terlalu lama.
