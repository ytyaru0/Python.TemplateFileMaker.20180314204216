import urllib.request
url = 'https://www.google.co.jp'
with urllib.request.urlopen(url) as res:
    print(res.read())
