import urllib.request

url = 'http://httpbin.org/basic-auth/user/passwd'
credentials = ('user', 'passwd')
auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password(realm='Test', uri=url, user=credentials[0], passwd=credentials[1])
opener = urllib.request.build_opener(auth)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
print("Response:", response.read().decode())
# Fungsi: Melakukan permintaan HTTP dengan otentikasi dasar.
# Kondisi: Ketika Anda perlu mengakses URL yang memerlukan otentikasi.
