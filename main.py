import requests
import socket
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)
r = requests.get(url)
print(r)
prop = "Previous Close"
print(r.status_code==200)
t = r.text
ind = (t.index("Previous Close"))
redtex = t[ind:].split("</span>")[1]
val = redtex.split(">")[-1]
print(val)