import requests
from selenium import webdriver
url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
r=requests.get(url)
print(r.status_code==200)
t=r.text
#print(t)
val = "BTC-UD"
if val in t:
    print("yes")
else:
     print("no")

driver = webdriver.Chrome(executable_path="C:/Users/91902/PycharmProjects/colurpicker/chromedriver")
driver.get(url)
ps=driver.page_source
#print(ps)
if val in ps:
    print("yes")
else:
     print("no")
#driver.close()