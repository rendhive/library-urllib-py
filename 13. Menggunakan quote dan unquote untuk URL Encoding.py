import urllib.parse

url = 'http://www.example.com/query?name=John Doe'
encoded_url = urllib.parse.quote(url, safe='/:?=')
print("Encoded URL:", encoded_url)

decoded_url = urllib.parse.unquote(encoded_url)
print("Decoded URL:", decoded_url)
# Fungsi: Mengkodekan dan mendekodekan bagian dari URL.
# Kondisi: Ketika Anda perlu mengelola karakter khusus dalam URL.
