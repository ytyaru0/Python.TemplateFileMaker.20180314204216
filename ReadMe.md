# このソフトウェアについて

テンプレートファイルを作成する。

# 目的

とにかくコードを書いてやってみるとき、適当なテンプレートコードが欲しい。お約束を何度も書くのが嫌なので。

# 使い方

```sh
python3 TemplateFileMaker.py
```
```sh
python3 TemplateFileMaker.py {path} {ext} {category1} {category2} {category3} ...
```
## 位置引数

i|略|意味
-|--|----
0|{path}|対象ファイルのフルパス
1|{ext}|対象ファイルタイプ
2..|{category}|テンプレートタイプ。順序は階層をあわらす

### {ext}

* py, sh, md, js, html, css, cs, ...

拡張子。プログラミング言語。バージョンによる言語の違いもある。どうするか。

### {category}

#### {category1}

{category1}|値
-----------|--
context|HTTP, DB, Server, ...
syntax|if, for, var, func, class, ...
built-in|id(), int(), hex(), str(), sorted(), ...

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

