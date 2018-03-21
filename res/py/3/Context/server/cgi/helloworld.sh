python3 -m http.server --cgi

# プロセス終了するときはpsとkillコマンドを使う
#
# $ ps aux | grep 'http'
#
# pi        4114  0.3  0.6  15288  5828 pts/2    S+   10:25   0:00 python3 -m http.server 8000
# pi        4158  0.0  0.1   3776  1832 pts/0    S+   10:27   0:00 grep http
#
# $ kill 4114
#
# (Ctrl + C で強制終了すると再起動できなくなるので注意)
