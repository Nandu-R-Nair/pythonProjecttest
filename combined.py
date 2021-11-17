import csv
import requests
import os.path
import pandas as pd
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
#print(tickerSymbol)
#print(len(tickerSymbol))
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

response = requests.get(url)
t = response.text

soup = BeautifulSoup(t,features="html.parser")
finalName= "1y Target Est"

trs = soup.find_all("tr")
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

#print(names)
#print(values)
#print(nameVal)
key_name = list(nameVal)
#print(key_name)
'''for i in range(len(key_name)):
    print(key_name[i])'''
file_path = 'C:/Users/91902/PycharmProjects/pythonProjecttest/data.csv'
if (os.path.exists(file_path)==True):
    pass
else:
    f = open('C:/Users/91902/PycharmProjects/pythonProjecttest/data.csv', 'w')
    writer = csv.writer(f)
    key_name.insert(0,"symbol")
    writer.writerow(key_name)
for i in range(30):
    print(tickerSymbol[i])
    site = tickerSymbol[i]
    url = "https://finance.yahoo.com/quote/"+site+"?p="+site+"&.tsrc=fin-srch"

    response = requests.get(url)
    t = response.text

    soup = BeautifulSoup(t, features="html.parser")
    finalName = "1y Target Est"

    trs = soup.find_all("tr")
    names = []
    values = []
    nameVal = {}

    # print(len(trs))
    for i in range(len(trs)):
        for j in range(len(trs[i].contents)):
            if j == 0:
                try:
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
        nameVal[name] = value
        if name == finalName:
            break
    val_name = list(nameVal.values())
    #print(val_name)
    if (os.path.exists(file_path) == True):
        f = open('data.csv', 'a',newline='')
        #print("inside")
        val_name.insert(0,site)

        writer = csv.writer(f)
        writer.writerow(val_name)





