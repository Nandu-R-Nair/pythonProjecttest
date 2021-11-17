import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

response = requests.get(url)
t = response.text

soup = BeautifulSoup(t,features="html.parser")
finalName= "1y Target Est"

trs = soup.find_all("tr")
#for i in range(0,7):
#tr2 = trs[0].find_all("td")
##for i in range(0,14):

  #  print(tr2[i].text)
#print(trs[0].contents[0].text)
#print(trs[0].contents[1].text)
#print(trs[1].tr.contents[0].text)

names = []
values = []
nameVal = {}

#print(len(trs))
for i in range(len(trs)):
    for j in range(len(trs[i].contents)):
        if j == 0:
            try :
                name = trs[i].contents[j].text
                names.append(name)
            except:
                continue

        if j == 1:
            try:
                value = trs[i].contents[j].text
                values.append(value)
            except:
                continue
    nameVal[name]=value
    if name == finalName:
        break



print(names)
print(values)
print(nameVal)


