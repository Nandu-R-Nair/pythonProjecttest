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
ind2 = (t.index(("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")))
print(ind2)
redtex = t[ind:].split("</span>")[1]
val = redtex.split(">")[-1]
print(val)
redtex2 = t[ind2:ind2+67].split('49">')[1]
print(redtex2)