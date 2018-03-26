# テンプレ引数の候補表示

include 文にひとつのテンプレ変数があるとき、入力候補を取得したい。

## 変数がひとつのときだけでいい理由

コマンド入力時、短くしたい。ファイル名のみが最善。変数ひとつで十分。

* include 構文
    * 変数なし: 入力候補なし
    * 変数あり: 入力候補あり
        * `"md/env/ + e + ".md"`
            * `path.glob("md/env/*.md")` が入力候補
                * 変数`e`に`/`を入れれば、`path.glob("md/env/**/*.md")` も入力候補になる
        * 入力候補: `-e: [ras_py, mint17_py, ...]`

* 複数の変数があるとき
    * `"md/env/ + e + d + ".md"`
        * e
            * `path.glob("md/env/*/")` が入力候補
        * d
            * `path.glob("md/env/**/*.md")` が入力候補
                * eも含むのでeの意味がない

## どんな表示？

### 前提条件

以下のテンプレがあるとする。

./templates/md/artifact.md
```markdown
## 開発環境

{% include "md/env/" + e + ".md" %}

## ライセンス

{% include "md/license/" + l + ".md" %}
```

どのテンプレをincludeするか、ファイル名を変数で受け取って決めるとする。

* ./templates/
    * md/
        * env/
            * ras_py.md
            * mint_py.md
        * licenses/
            * CC0-1.0.md
            * mit.md

このとき、変数`e`, `l`の候補を表示したい。

```sh
$ do md artifact<ENTER>
テンプレート変数が不足しています。たとえば以下のように入力してください。
do md artifact -e ras_py -l CC0-1.0

各変数の入力候補は以下の通り。
-e: [ras_py, mint_py]
-l: [CC0-1.0, mit]
```

テンプレのカテゴリは`complete`, `compgen`で候補を表示している。だが、テンプレ変数では不可能。なぜなら同時に複数の変数がありうるから。また、カテゴリ名と一緒くたに表示すると混乱する。

もし、コマンド置換により`md`で`md/artifact.md`を示すように指示した場合、`compgen`での表示が以下のようになりうる。

```sh
$ do md <TAB>
env  license  -e  -l
```

本当は確定前に表示したいのだが、`complete`, `compgen`以外の方法を知らない。仕方ないのでエラー状態で確定させたあとに表示させる。

