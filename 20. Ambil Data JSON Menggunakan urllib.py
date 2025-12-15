import urllib.request
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    print("JSON data:", data)
# Fungsi: Mengambil data JSON dari URL dan mengubahnya menjadi objek Python.
# Kondisi: Ketika Anda perlu mengambil dan memproses data JSON dari API.
