import urllib.parse

params = {'search': 'python', 'page': 1}
encoded_params = urllib.parse.urlencode(params)
print("Encoded Parameters:", encoded_params)
# Fungsi: Mengubah dictionary menjadi query string untuk URL.
# Kondisi: Ketika Anda ingin mengirim data melalui URL dalam format query.
