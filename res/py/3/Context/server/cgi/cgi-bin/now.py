#!/usr/bin/python3
#!/home/pi/root/env/py/auto_github/bin/python
# ↑「FileNotFoundError: [Errno 2] No such file or directory: 」のエラーが出る場合、シェバング行のパスが合っていない可能性が高い
# http://goldilocks-engineering.blogspot.jp/2015/11/pythoncgi.html
import datetime
html_body = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello CGI !!</title>
</head>
<body>
    <p>アクセス日時は<datetime>%s</datetime>です。</p>
</body>
</html>
"""
print("Content-type: text/html;charset='UTF-8'\n")
print(html_body % ('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())))

#import cgi
#form = cgi.FieldStorage()
#text = form.getvalue('text','')

