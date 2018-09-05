import urllib.request
import bs4 as bs
import os
link = 'https://en.wikipedia.org/wiki/Deep_learning'
source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source)
print(soup.title.text)
for url in soup.find_all('a'):
    print(url.get('href'))
