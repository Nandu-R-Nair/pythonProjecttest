import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

response = requests.get(url)
t = response.text

soup = BeautifulSoup(t,features="html.parser")

trs = soup.find_all("tr")

print(trs[0].contents[1])