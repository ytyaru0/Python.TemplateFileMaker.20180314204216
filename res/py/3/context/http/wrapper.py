import requests
url = 'https://www.google.co.jp'
res = requests.get(url)
res.raise_for_status()
print(res.text)

