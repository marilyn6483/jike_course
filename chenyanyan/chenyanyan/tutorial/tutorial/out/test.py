# -*- coding: utf8 -*-
import re
from bs4 import BeautifulSoup
with open("page2", 'rb') as r:
    html = r.read()

html = re.sub("&lt;", "<", html)
html = re.sub("&gt;", ">", html)
soup = BeautifulSoup(html, 'lxml')
all_a = soup.find_all(name="a", attrs={"class": "poi-tile__head J-mtad-link"})
urls = list()
for a in all_a:
    urls.append(a['href'])
print len(urls)
print a
p = a.findNext(name='span', attrs={"class": "price"}).text
p = re.sub("^.", "", p)
print p
