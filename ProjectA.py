import requests
url = "http://172.17.50.43/multi"
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t",r.status_code)
h = requests.head(url)
print("Header:\n headers.php")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("headers.php")

url2 = "http://172.17.50,43/headers.php"
header = {
    'User-Agent':'Mobile'
}
r2 = requests.get(url2,headers = headers)
print(r2.text)