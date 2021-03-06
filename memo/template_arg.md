# テンプレ引数

かなり複雑になってしまう。実装するかどうかは要検討。

## 変数

テンプレートに引数を渡したいことがある。

### 位置引数

テンプレートは以下のようにする。

./template/py/_MIN.py
```python
class ${0}:
    pass
```

と思ったが、`${}`はshellにおける変数参照のプレースホルダーとして使われている。`<% %>`なら使われにくい。可読性も低いが。

```sh
echo ${0}
echo {{0}}
echo <%0%>
```

以下のように`$`でテンプレ変数の値を指定する。
```sh
$ do py _MIN $MyClass
```

と思ったが、`$`はshellにおけるメタ文字で変数参照の意味がある。`$`のかわりに`-`を使う。

```sh
$ do py _MIN -MyClass
```

もし`<%%>`を使うなら`%`でもいいか。

```sh
$ do py _MIN %MyClass
```

テンプレートファイル名やディレクトリ名、コマンド名の先頭には`-`が使えなくなる。

出力結果は以下。
```python
class MyClass:
    pass
```
引数が複数あるときは出現順がインデックスになる。

### キーワード引数

./template/py/_MIN.py
```python
class ${Name}:
    pass
```

以下のように`-`でテンプレ変数名を指定し、つぎに値を渡す。
```sh
$ do py _MIN -Name MyClass
```

出力結果は以下。
```python
class MyClass:
    pass
```

`$`ではじまる引数はテンプレート変数名とする。次の位置にある引数は、その値とする。

### 引数の表記例

```sh
$ do py _MIN -Value1 -Value2 -Value3
```
```sh
$ do py _MIN -Key1 Value1 -Key2 Value2 -Key3 Value3
```

位置引数とキーワード引数の併用はできない。テンプレートは必ずどちらか一方のみを使う。併用を許すととても複雑になるため。

以下はボツ。一般的でないため。

```sh
$ do py _MIN -Key=Value
```
```sh
$ do py _MIN -"Value1 Value2"
```
```sh
$ do py _MIN -"key1=Value1 key2=Value2"
```
```sh
$ do py _MIN -"key1:Value1 key2:Value2"
```

## 引数パターン

### 位置引数とキーワード引数

変数名|種類|テンプレ例|コマンド例
------|----|----------|----------
${[0-9]+}|位置引数|${0}, ${10}|`$ do py $Val0 $Val1 $Val2`
${[a-zA-Z][a-zA-Z0-9_]+}|キーワード引数|${Name}|`$ do py $Name Andy $Key Val`

### 省略時自動リプレース

変数名|種類|テンプレ例|コマンド例
------|----|----------|----------
${変数名:デフォルト値}|略時自動置換|${0:A}, ${Name:A}|`$ do py`

`${変数名:デフォルト値}`でテンプレート引数を省略したときに置換される値を設定できる。

`${0:A}`とすると、一番目の位置引数を省略したときは、その部分が`A`に置換される。キーワード引数も同様。

デフォルト値には何でも指定できるが、[メタ文字](#メタ文字)を使うときはエスケープが必要。

### 自動リプレース

テンプレートに埋め込んでおくと作成時に自動的に値をセットしてくれる。コマンド引数不要。

変数名|種類|テンプレ例|コマンド例
------|----|----------|----------
${%?}|日時|${%Y年%m月%d日 %H時%M分%S.%f秒}|`$ do py`

日付はファイル作成時点でのシステム現在時刻。`datetime.datetime.now()`とする。

### インクルード

変数名|種類|テンプレ例|コマンド例
------|----|----------|----------
${.*[/.]+.*}|パス|${/tmp/template.py}|`$ do py`

なお、パスについては以下の3通りある。

例|相違
--|----
`/tmp/template.py`|絶対パス
`./template.py`|相対パス（そのテンプレートファイルからの）
`py/template.py`|相対パス（テンプレートROOTディレクトリからの）

テンプレROOTからの参照は、先頭が`/`, `./`, `../`でなく、かつ`/`と`.`がひとつ以上含まれていること。

相対パスは以下のようにも使える。

* `./some/template.py`
* `../template.py`
* `../../template.py`
* `../some/template.py`

以下のように`/`がひとつもないときは、相対パスとしてみる。ROOTディレクトリからではなく、そのテンプレファイルからの相対パスとして。

* `template.py`

なお、取込先テンプレに引数を渡したいときがある。以下のようにする。

```
${テンプレのパス:コマンド引数}
```

# くわしく

## デフォルト値

変数の値にデフォルト値を指定したいこともある。

* ${0}=`A`
* ${Name}=`A`

${0}や${Name}がテンプレ内にあるのに、起動引数から省略されたとき、`A`に置換する。

外部ファイルでシステム全体の設定ができるようにするといいかも。

~/root/_meta/command/do/template_default.ini
```ini
[Default]
Name=A
```

### 任意のデフォルト値

テンプレ内で定義する。
```python
class ${Name:A}:
    pass
if __name__ == '__main__':
    c = ${Name}()
```
一度定義されたら、ほかの場所でもそのデフォルト値を使う。

以下のようにコマンド引数を指定したのと同じになる。
```sh
$ do py $Name A
```
上記の設定をせず、以下のコマンドで同様の結果が得られる。
```sh
$ do py
```
もし、デフォルト値以外を使いたければ、引数を指定すればいい。

## インクルード

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

`/`または`.`を含むときはテンプレート取込と判断する。

`./`の値ではじまるものは別テンプレート取込とする。

### 取込テンプレ選択

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

#### 複数

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

#### テンプレ変数の入力候補

テンプレ変数の入力候補が知りたい。だが、キーワード変数が複数あるとcompgenでは機能不足。順序に関係なくテンプレ変数とその候補をすべて表示したい。（ヘルプに近い）

```sh
$ do md artifact <TAB>
  $env: ras
    ras-py ras-node
  $license: cc0-1.0
    mit apatch-2.0
```

位置引数だったとしても、一度に表示したい。

```sh
$ do md artifact <TAB>
  $0: ras
    ras-py ras-node
  $1: cc0-1.0
    mit apatch-2.0
```

##### 取込テンプレに変数があった場合

元のテンプレと取込先テンプレの両方に変数があったとき、両者の区別ができない。

以下のテンプレがあるとする。

./py/class.py
```python
class ${0}: pass
${./function.py}
```
./py/function.py
```python
def ${0}():
    pass
```

以下のコマンドでファイル作成したとき。

```sh
$ do py class $MyClass
```

以下のような結果になってしまう。

```python
class MyClass: pass
def MyClass():
    pass
```

###### 取込先テンプレ引数

元テンプレ側で取込先テンプレに引数を渡す案が考えられる。

```python
class ${0}: pass
${./function.py:${0}_func}
```

```python
class MyClass: pass
def MyClass_func():
    pass
```

引数が複数あったりキーワード引数だったときは、さらに複雑になる。基本は以下。

```
${テンプレのパス:コマンド引数}
```

元テンプレが受けたキーワード変数を渡したいときの表現がバッティングする問題がある。以下の場合、`$Key`は元テンプレが受けた変数名を渡した位置引数なのか、取込先テンプレのキーワード引数の変数名なのか区別がつかない。

* `${./function.py:$Key Value}`

これを解決するためには、テンプレ側で`{}`の省略を禁止にすればいい。コマンド側では`{}`を省略した記法しか使えず、テンプレ側では`{}`をつけた記法しか使えないようにすれば区別可能。

`shlex.split()`でうまいこと引数を区切ってくれそうか。

* `${./function.py:${0} some}`
* `${./function.py:$Name Value $Key Value}`
* `${./function.py:"V A L U E"}`
* `${./function.py:"${0} V A L U E"}`
* `${./function.py:"\"${0} V A L U E\""}`
* `${./function.py:"\"${0} V A L U E\"" "A B"}`

## コマンドのプレフィクス

prefix|意味
------|----
`(なし)`|テンプレのカテゴリ
`-`|オプション。フラグ。または値をもつ（次の位置引数）
`$`|テンプレ変数。値。またはキーと値。出現順がインデックスになる。

## メタ文字

メタ文字|意味
--------|----
`$`|変数開始
`{`,`}`|変数の開始と終了
`%`|日時フォーマット用
`:`|変数名と設定値のデリミタ
`/`, `.`, `*`|ファイルパス用

### エスケープ

メタ文字自体をテンプレートのテキストとして使いたいときはエスケープする必要がある。

`\`をメタ文字の前につけることでエスケープできる。

### 引数の位置

* 引数の種類
    * `-`系
    * `$`系
    * テンプレートカテゴリ

テンプレートカテゴリは、連続しているべき。間にほかの引数をいれてもカテゴリ名として認識される。

-,$系引数は、カテゴリの前にすべき。

# 既存テンプレエンジン参考

* include, extends, mixin
    * https://necosystem.hirokihomma.com/archives/121/
* jinja2
    * http://www.python.ambitious-engineer.com/archives/760

## include

./template1.py
```
<% include template2.py %>
if __name__ == '__main__':
    pass
```

./template2.py
```
class <% 0 %>: pass
```

./template1.py の結果は以下。
```
class <% 0 %>: pass
if __name__ == '__main__':
    pass
```

```sh
$ do py -MyClass
```
```python
class MyClass: pass
if __name__ == '__main__':
    pass
```

## extends

./template1.py
```
class <% 0 %>: pass
```

./template2.py
```
<% extends template1.py %>
<% 0 %> MyClass
```

```sh
$ do py
```

出力結果
```
class MyClass: pass
```

変数の値をセットする。コマンド入力でなくテンプレファイルに。

## mixin

py_class.mixin
```
<% mixin Class(name) %>
class <% name %>: pass
```

./template1.py
```
<% include py_class.mixin %>
%Class('MyClass1')
%Class('MyClass2')
%Class('<% 0 %>')
```

展開結果。
```
class MyClass1: pass
class MyClass2: pass
class <% 0 %>: pass
```

```sh
$ do py AAA
```

展開結果。
./template1.py
```
class MyClass1: pass
class MyClass2: pass
class AAA: pass
```

# 蛇足

以下。蛇足。考えた経緯。ボツ案。

-------------------------------------------------------------------

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
