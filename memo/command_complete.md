# command_complete

complete, compgen, コマンドで入力候補の表示と補完をする。

設定ファイルを読み込んで、テンプレファイルとコマンドを紐付ける。コマンド情報から、complete, compgen, コマンドによる.shファイルを作成する。それを source として読み込ませることで補完させる。

doコマンド保管用.shファイルを/tmp/work/.meta/flow/do/complete.shに作成する。
doコマンドはこのファイルを source として読み込むと入力補完できる。

complete.shはpythonプログラムで作成する。
