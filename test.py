import requests
from bs4 import BeautifulSoup

# r = requests.get("https://tuoitre.vn/the-thao.htm")
# txt = BeautifulSoup(r.text, 'html.parser')
# data = txt.find_all('h3', {'class':'box-title-text'})
# for link in data:
#     print('https://tuoitre.vn'+link.a.get('href'))


r = requests.get("https://twitter.com/home")
txt = BeautifulSoup(r.text, 'html.parser')
data = txt.find_all('div')
print(txt.prettify())
