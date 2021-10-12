import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

response = requests.get(url)
t = response.text

soup = BeautifulSoup(t,features="html.parser")

trs = soup.find_all("tbody")
#for i in range(0,7):
tr2 = trs[0].find_all("td")
for i in range(0,14):

    print(tr2[i].text)
#print(trs[0].contents[0].span.text)
#print(trs[0].contents[0].td.text)
#print(trs[1].tr.contents[0].text)
