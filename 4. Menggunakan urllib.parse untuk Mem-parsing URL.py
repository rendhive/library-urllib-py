import urllib.parse

url = 'http://www.example.com/path?query=example#fragment'
parsed_url = urllib.parse.urlparse(url)
print("Parsed URL:", parsed_url)
# Fungsi: Mem-parsing URL menjadi komponen-komponen terpisah.
# Kondisi: Ketika Anda perlu menganalisis situs internet dan mendapatkan komponen yang berbeda.
