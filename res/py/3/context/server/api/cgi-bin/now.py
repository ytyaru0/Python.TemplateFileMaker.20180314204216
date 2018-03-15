#!/usr/bin/python3
#!/home/pi/root/env/py/auto_github/bin/python
# ↑「FileNotFoundError: [Errno 2] No such file or directory: 」のエラーが出る場合、シェバング行のパスが合っていない可能性が高い
# http://goldilocks-engineering.blogspot.jp/2015/11/pythoncgi.html
import cgitb
cgitb.enable()

import datetime
import json
ret = dict(now='{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
print("Content-type: application/json;charset='UTF-8'\n")
print(json.dumps(ret))

#import cgi
#form = cgi.FieldStorage()
#text = form.getvalue('text','')

