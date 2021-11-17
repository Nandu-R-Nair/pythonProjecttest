import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(url)
t = response.text
print(response.status_code)
#print(t)
soup = BeautifulSoup(t,features="html.parser")
#finalName= "1y Target Est"

trs = soup.find_all("tbody")
trs2 = trs[0].find_all("tr")
tickerSymbol = []
#print(trs2)
for i in range(1,len(trs2)):
    symbol = trs2[i].contents[1].text
    #print(symbol)
    symbol =symbol.replace('\n','')
    tickerSymbol.append(symbol)
print(tickerSymbol)
