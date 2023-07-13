from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://nofluffjobs.com"
page  = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")

print(soup.get_text())
print(soup.find_all("img"))