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

KeyValue形式。TABをメタ文字とする。

commands.tsv
```
py/3/context/ui/c/_ALL.py   py cui
py/3/context/ui/c/_MIN.py   py cui min
py/3/context/ui/c/main.py   py cui main
py/3/context/ui/c/args.py   py cui args
py/3/context/ui/c/shell.py  py cui shell
...
```

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
_DEFAULT.{ext}|command省略時に使うテンプレ。利用頻度の高い内容にすべき
_MIN.{ext}|最小テンプレ
_MAX.{ext}|最大テンプレ

* コマンド引数のコンプリート候補には表示されない
* 必須ではなく任意
* 各カテゴリ配下にひとつずつ配置可能
* コマンド引数省略時、上記の優先順に参照される
    * ひとつもないならカテゴリ（実行してもテンプレファイル未存在エラー）

`$ do py`を実行したとき、`./template/py/_DEFAULT.py`のテンプレートファイルが使用される。

コマンド|使用テンプレ
--------|-----------
`$ do py`|`./template/py/_DEFAULT.py`
`$ do -min py`|`./template/py/_MIN.py`
`$ do -max py`|`./template/py/_MAX.py`
`$ do -random py`|`./template/py/**/*.py`

## 候補と補完

https://qiita.com/sosuke/items/06b64068155ae4f8a853

complete, compgen コマンド。

## テンプレ引数

かなり複雑になってしまう。実装するかどうかは要検討。

### 変数

テンプレートに引数を渡したいことがある。

./template/py/_MIN.py
```python
class ${Name}:
    pass
```

```sh
$ do -min $Name MyClass py
```

`$`ではじまる引数はテンプレート変数名とする。次の位置にある引数は、その値とする。

#### デフォルト値

変数の値にデフォルト値を指定したいこともある。

* ${Name}=`A`

${Name}がテンプレ内にあるのに、起動引数から省略されたとき、`A`に置換する。
これは最小テンプレに合わせたもの。

##### 任意のデフォルト値

テンプレ内で定義する。
```python
class ${Name:A}:
    pass
if __name__ == '__main__':
    c = ${Name}()
```
一度定義されたら、ほかの場所でもそのデフォルト値を使う。

#### 引数省略形

テンプレートファイル内にひとつしか変数がないとき、以下のように略記可。

```sh
$ do py class $MyClass
```

先頭に`$`がついていたらテンプレート変数の値と断定する。

ただし、変数が2つ以上あるときは使えない。


### 現在日時

テンプレートに現在日時を任意の書式で記入したいことがある。

```markdown
* 作成日時: ${datetime.datetime.now():%Y年%m月%d日 %H時%M分%S秒}
```
```markdown
* 作成日時: ${Now:%Y年%m月%d日 %H時%M分%S秒}
```

左辺がある分、複雑になる。`%Y`など`%`がついていたら日付と判断する。

```markdown
* 作成日時: ${%Y年%m月%d日 %H時%M分%S秒}
```
```markdown
copyright ${%Y} ${Author}
```
#### コマンドによる解決

```sh
$ do md artifact $date "%Y-%m-%d %H:%M:%S.%f"
```

テンプレ変数値に`%`がついた文字が渡されると、日時フォーマットとして解釈。対象時刻は現在日時とする。

テンプレ解析は楽になるが、コマンド入力が面倒になる。現実的でない。

### ループ

```sql
insert into Humans(Id,Name) values(${0}, ${1})
```
```tsv
0   Tarou
1   Jirou
2   Saburou
```
```sh
$ do sql insert columns $$./param.tsv
```

不要か。テンプレートは一度に繰り返し同じものを量産するのは本意ではない。

### インクルード

ほかのテンプレートを取り込みたいときがある。

./md/artifact.md
```markdown
# 成果物

# 開発環境

${./md/env/ras.md}
```

./md/env/ras.md
```markdown
* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](http://ytyaru.hatenablog.com/entry/2016/12/01/100000) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000) 1.2.1
            * Python 3.6.4
```

`./`の値ではじまるものは別テンプレート取込とする。

#### 取込テンプレ選択

どのテンプレを取り込みたいか選択したいことがある。

```sh
$ do md artifact ras
```

./md/artifact.md
```markdown
# 成果物

# 開発環境

${./md/env/*.md}
```

正規表現`./md/env/*.md`に該当するファイルのうちどれかひとつを追加したい。

このとき、起動引数のコンプリート候補に出したい。指定がなければエラーを表示し、引数の入力を促す。

_MIN.md, _MAX.md, _DEFAULT.md, の特殊テンプレを使いたいときはどうするか。省略時は_DEFAULT.mdを使ってしまっていいのか。

##### 複数

複数あった場合、名前をつけて対応する。

```sh
$ do md artifact $env ras $license cc0-1.0
```

./md/artifact.md
```markdown
# 成果物

# 開発環境

${env:./md/env/*.md}

# ライセンス 

${license:./md/license/*.md}
```

### コマンドのプレフィクス

prefix|意味
------|----
``|テンプレのカテゴリ
`\`, `!`|オプション。フラグ。スイッチ。
`-`|オプション。値をもつ（次の位置引数）
`$`|テンプレ変数。値をもつ（次の位置引数）

### メタ文字

メタ文字|意味
--------|----
`$`|変数開始
`{`,`}`|変数の開始と終了
`%`|日時フォーマット用
`:`|変数名と設定値のデリミタ

#### エスケープ

メタ文字自体をテンプレートのテキストとして使いたいときはエスケープする必要がある。

`\`をメタ文字の前につけることでエスケープできる。

## 引数の位置

* 引数の種類
    * `-`系
    * `$`系
    * テンプレートカテゴリ

テンプレートカテゴリは、連続しているべき。間にほかの引数をいれてもカテゴリ名として認識される。

-,$系引数は、カテゴリの前にすべき。

