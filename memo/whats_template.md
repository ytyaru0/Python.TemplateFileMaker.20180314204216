# テンプレートとは一体

何だったのか。改めて考えてみる。

<!-- more -->

# これぞテンプレ

## 固定テキスト

template.py
```python
if __name__ == '__main__':

```

お決まり、お約束の固定テキスト。使いまわす奴。

## 穴埋め

template.py
```
class {{ Name }}:
    def __init__(self):
        pass
    def Run(self):
        print('Hello World !!')

if __name__ == "__main__":
    c = {{ Name }}:
    c.Run()
```

* テンプレファイルをみればどんな内容かひと目でわかる
    * クラス名だけ渡せば、速攻でpythonコードが書けるテンプレ

ほとんどプレーンテキストだが、ごく一部を穴埋めするもの。フォーマット、フレームワーク、などの言葉と似た意味がある。

ここに`if`,`for`などの制御文を入れたらもうテンプレじゃない。`include`すらNG。単一ファイルで完結させたい。

## テンプレを逸脱した要求

### include

複数箇所で共有すべき内容で、管理を一元化したいなら、DRYに書けるようincludeしたい。

DRYに書きつつ、出力結果がパッと見すぐ見たい。これらを両立するにはどう解決すればいい？　専用エディタが必要？　そもそも、共通部分が存在しないようにテンプレを作るべき？　後者ならテンプレエンジンの存在意義が無くならない？

テンプレは部分置換するだけのプレーンテキストファイルであるべきか。

### デフォルト値

jinja2はテンプレ変数が渡されなければ空文字列として出力される。

デフォルト値をテンプレ内で定義したい。

#### 変数名そのまま

変数値がわたされなかったら変数名をそのまま出力したい。

#### 挙動の指定

jinja2のデフォルトでは変数値がわたされなかったら空文字列だが、どうするかを選びたい。

* 空文字列に置換
* 指定値に置換
* エラー発生

### エラーメッセージ

デフォルト値がなければ必須とみなす。必須なのに渡されなければエラーメッセージを表示したい。

### バリデーション

入力値が所定の条件かどうか判定したい。違反していたらエラーメッセージを表示したい。

正規表現とか使いたい。もはや構文の構築か。

## デフォルト値

### A. 埋め込み（インライン）

以下のようにすると`Name`のデフォルト値を`AAA`に設定できるといいな。

template.py
```
class {{ Name:AAA }}:
    def __init__(self):
        pass
    def Run(self):
        print('Hello World !!')

if __name__ == "__main__":
    c = {{ Name }}:
    c.Run()
```

メタ文字を使う場合などは`{{ Name:": A B\nC" }`のようにクォーテーションで囲むとか。

### B. 埋め込み（ブロック）

template.py
```
class {{ Name }}:
    def __init__(self):
        pass
    def Run(self):
        print('{{ Message }}')

if __name__ == "__main__":
    c = {{ Name }}:
    c.Run()
{% default yaml %}
Name: AAA
Message: Hello World !!
{% enddefault %}
```

一気にコードが汚くなる。形式は`yaml`, `toml`, `json`, `xml`, `ini`から選べる。

### C. 外部ファイル

template.default.yml
```
Name: AAA
Message: Hello World !!
```

テンプレファイルと同一ディレクトリに配置。名前に規則をもたせて自動的に対応づける。

## 値によって変えたい

Messageは1行のときは`'{{ Message }}'`, 複数行のときは`"""{{ Message }}"""`としたい。

template.default.yml
```yaml
Name: AAA
Message: |
    Hello
    World !!
```

```python
def Quote(item, item_type):
    if item_type == 'single-line-text': return "'" + item + "'"
    elif item_type == 'multi-line-text': return "'''" + item + "'''"
    else: return str(item)

template.injection(Message=Quote)
template.render(yaml.load('template.default.yml'))
```

ところで、これはもはやプレーンテキストのテンプレとして対応すべき領域をこえていないか？ `'`、`'''`はpython構文。pythonコードを出力したいなら、python構文にしたがってコード出力するのが自然では？

つまり、プログラミングのソースコードを出力したいなら、各プログラミング言語の構文体系に則って出力すべき。そのために別途プログラミングすべき。無理にテンプレートエンジンに頼ると汚いテンプレができあがるし、言語仕様の変更に対応できない。

ただ、その方法がわからないし、割に合わない労力をかけるハメになりそうな予感。

### 継承クラスのテンプレ

任意のクラスの全インタフェースを継承したクラスを自動生成したい。

もはやテンプレではない。コードヘルパー？ インテリセンス？ サジェスト？

```python
class ObjectSub(object):
```

`object`クラスの継承クラス。`object`のもっている全メソッドを網羅したい。そして、そのソースコードを出力したい。

どんなインタフェースを持っているか知りたいときにも便利そう。`dir(object)`だと引数がわからない。CPythonなら組込クラスはたぶんC言語実装。

ちゃんとやるなら、以下ライブラリを使うべきか。

* [https://docs.python.jp/3/library/language.html:title]
    * [https://docs.python.jp/3/library/ast.html:title]

非常に面倒そう。Pythonのバージョンによって言語仕様とともに変更される。

# 所感

テンプレとすべきものもあれば、プログラミングでテキストを出力したほうがいいものもある。出力するテキストに応じて、どうすべきか判断が必要。

テキスト生成方法が異なっても、同一インタフェースで制御できるシステムって無いかな？　jinja2の機能にあるのかな？

[http://jinja.pocoo.org/docs/2.10/api/]

API一覧みてもよくわからん。
