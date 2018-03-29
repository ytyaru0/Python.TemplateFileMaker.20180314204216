# テンプレート引数がないときの挙動

どうするか。たとえば、必須か任意か。任意ならデフォルト値は何か。

## jinja2

* `{{Name}}`のように変数の場合、`jinja2.Template.render()`で`Name`が渡されなかったときは、空白になる
* `{% include "md/env/" + e + ".py" %}`のとき、`e`は未定義エラーになる。`jinja2.exceptions.UndefinedError`

統一性がとれていない。では、どうあるべきなのか？　テンプレートエンジンには想定しうる罠がかなり沢山ありそう。まずはそれを整理したい。

## テンプレエンジンの罠

* includeしたときのテンプレ変数
    * 元テンプレの変数と被る
        * 同一名の変数だが、別の値を設定したいときに困る

解決するにはjinja2の`macro`を使うべき。

### macro

* 関数。引数やそのデフォルト値を指定できる
    * `{% macro some(p1, p2='') -%}`, `{%- endmacro %}`, で囲まれた部分がマクロになる
    * `{{ p1 }}`のように引数を使う
* `{% import "macro.jinja" as m %}`で外部ファイル化した`macro`を取り込める

以下の長所がある。

* テンプレを重複なくDRYに書ける
* デフォルト値を指定できる

以下の短所がある。

* 生のテキストが見えない（テンプレートなのに出力形式が見えない）

## 例

```python
class {{ Name }}: pass
```

上記のテンプレを以下の条件で使いたい。

* 省略した場合は`A`。そして設定方法メッセージを表示したい

class.py
```python
{% macro define(Name='A') %}
class {{ Name }}:
{% endmacro }
```

class_blank.py
```python
{% import "py/Syntax/class.py" as cls %}
{{ cls.define(MyClass) }}
    pass
```
