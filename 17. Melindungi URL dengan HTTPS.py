import urllib.request

url = 'https://www.example.com'
try:
    response = urllib.request.urlopen(url)
    print("Data fetched successfully over HTTPS.")
except Exception as e:
    print("Error:", e)
# Fungsi: Mengakses URL yang menggunakan HTTPS untuk komunikasi aman.
# Kondisi: Ketika Anda ingin memastikan bahwa data diambil secara aman.
