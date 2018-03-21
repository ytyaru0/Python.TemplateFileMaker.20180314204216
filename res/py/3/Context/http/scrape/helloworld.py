import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.google.co.jp'
with urllib.request.urlopen(url) as res:
    soup = BeautifulSoup(res.read(), 'html.parser')
    print(soup.select('title')[0].text) # `<title>*</title>`
