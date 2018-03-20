# command名

* テンプレとコマンド名の紐付ファイルが欲しい
    * 使っているうちに変わっていくから
* 候補を表示して欲しい
    * どんなcontextがあるか知らないか忘れるから

## ディレクトリとコマンドの不一致
    
ディレクトリとコマンドが一致しているのが望ましいが、そうはいかない。

### テンプレ 

* py
    * 2
    * 3
        * context
            * ui
                * c
                    * min.py
                    * args.py
                    * main.py
                    * parse.py
                    * shell.py
                * g
            * db
            * html
            * ...
        * syntax
        * degignpattern

### コマンド

```sh
$ do py cui
```

これで./ui/c/に属するすべてのテンプレを含んだファイルを作って欲しい。

### 紐付けファイル

1. テンプレファイルをすべて読み込む
1. ファイルを網羅する
1. 各ファイルにコマンドを割り当てていく

3はディレクトリ構成から自動割当される。それを元に手動で短縮形に変えていく。

### テンプレ識別子

要素|例
----|--
ext|py, sh, md, ...
version|2, 3, ...
context-group|context, syntax, designpattern, ...
context|http, db, server, ui, ...
sub-context|character, graphical, EntityFramework, ...
version|4.1, 6, ...
name|_MIN.py, _ALL.py, main.py, ...

ext, nameは必須。ほかは任意。

事実上、テンプレファイルを重複せず配置するためには複数のディレクトリ構造が必須。

### 予約名テンプレ

テンプレファイルにはいくつか特殊な名前を持ったものを用意する。

name|意味
----|----
_MIN|最小テンプレ
_ALL|最大テンプレ, MAX, FULL

