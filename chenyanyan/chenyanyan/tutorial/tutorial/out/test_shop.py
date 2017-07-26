import re
from bs4 import BeautifulSoup
with open("shop.html", 'rb') as r:
    html = r.read()

html = re.sub("&lt;", "<", html)
html = re.sub("&gt;", ">", html)
soup = BeautifulSoup(html, 'lxml')
t = soup.find(name="span", attrs={"class": "title"})
print t.text
t = soup.find(name="span", attrs={"class": "geo"})
print t.text
t = soup.find_all(name="p", attrs={"class": "under-title"})
print t[1].text
t = soup.find(name="span", attrs={"class": "biz-level"}).find(name="strong")
print t.text
t = soup.find(name="a", attrs={"class": "tag"})
print t.text
t = soup.find(name="a", attrs={"class": "num rate-count"})
print t.text
