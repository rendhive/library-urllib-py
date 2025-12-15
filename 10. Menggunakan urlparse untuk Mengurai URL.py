import urllib.parse

url = 'https://www.example.com/path?q=search#fragment'
parsed = urllib.parse.urlparse(url)

print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
print("Query:", parsed.query)
print("Fragment:", parsed.fragment)
# Fungsi: Mengurai URL dan menampilkan komponen.
# Kondisi: Ketika Anda ingin mendapatkan bagian dari URL untuk analisis lebih lanjut.
