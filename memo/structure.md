# 構造

* ~/.bashrc
    * python3 ~/root/script/_meta/path/IniToSh.py
    * . ~/root/script/_meta/path/sh/paths.sh
    * . setup_complete_candidate_do.sh
* ~/root/
    * _meta/
        * path/
            * ini/
                * path.ini
            * sh/
                * paths.sh
            * IniToSh.py
        * command/
            * do/
                * setup_complete_candidate.sh
                * command_replace.tsv
            * pj/
                * setup_complete_candidate_pj.sh
            * repo/
                * setup_complete_candidate_repo.sh
    * script/
        * sh/
            * _command/
                * do
        * py/
            * os/file/
                * NameGenerator.py
            * _command/
                * do/
                    * TemplateMaker/
                        * CommandReplaceFile.py
                        * CommandsFile.py
                        * CommandToTemplate.py
                        * ConfigFile.py
                        * do.py
                        * PathToCommand.py
                * pj/
                * repo/

* ~/root/db/
    * template/
        * _command/
            * do/
                * py/
                    * 2/
                    * 3/
                        * Context/
                            * hello.py
            * pj/
            * repo/

* /tmp/work/.meta/
    * _command/
        * do/
            * commands.tsv
            * command_replace.tsv

* /tmp/work/Python.TemplateFileMaker.20180314204216/res/
    * (テンプレート配置)

## RAM Disk

`/tmp/`はRAMディスクとする。
テンプレートが追加されるなどの変更があっても、tsvファイルの変更はメモリ上で保持される。SDカードやSSDへの書込は生じない。

### commands.tsv

`/tmp/work/.meta/_command/do/`配下にcommands.tsvを作成する。
commands.tsvはテンプレートファイルがあるディレクトリを捜査し、初回のみ作成する。
更新したいときはcommands.tsv、command_replace.tsvのファイルを削除してからdoコマンドを実行すること。

### command_replace.tsv

command_replace.tsv は手書き。自動作成できない。
`~/root/_meta/command/do/`配下に配置する。`/tmp/work/.meta/`に存在しなければそこへコピーし、そちらを読むようにする。一時的に変更したいとき、RAM Disk上でできる。

### テンプレート

`~/root/db/template`に配置する予定だが、まだディレクトリすら作成しない。

テンプレは日々加筆、修正することが予想される。完成するまではRAMディスクで読み書きpushしていきたい。

そこで、当面は以下のリポジトリ配下のディレクトリを使う。

* /tmp/work/Python.TemplateFileMaker.20180314204216/res/

## Python

doコマンドはshellでなくPython主体で実装されている。

よって、実行前にはPython設定スクリプトが必要。

* /tmp/work/RaspberryPi.Home.Root.20180318143826/src/script/sh/_called/bash/bashrc.sh

```sh
# 時刻同期できない問題: .bash_profileだとログイン後に自動実行されるが時刻同期されず。一時ファイルだけが作成されて以降実行されなくなってしまう。
. "$HOME/root/script/sh/_lib/env.sh"
ExportPath "$HOME/root/tool" "$HOME/root/script/sh/_command"
. ~/root/script/sh/mkdir_work.sh
~/root/script/sh/call_settime.sh
. ~/root/script/sh/pyenv.sh
. ~/root/script/sh/py_venv.sh

# ユーザパス設定読込
python3 /tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/IniToSh.py
. /tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/path/sh/paths.sh
#python3 ~/root/_meta/path/IniToSh.py
#. ~/root/_meta/path/sh/paths.sh

# コマンドの引数補完セット
. /tmp/work/RaspberryPi.Home.Root.20180318143826/src/_meta/command/do/setup_complete_candidate_do.sh
#. /tmp/work/Python.TemplateFileMaker.20180314204216/src/setup_complete_candidate_do.sh
#. ~/root/_meta/command/setup_complete_candidate_do.sh
```

### テンプレートエンジン

jinja2を使う。これに伴い、doコマンド実行には仮想環境のactivateが必要。

* `~/root/env/py/template/bin/activate`

doコマンドスクリプト内で呼び出す。

* ~/root/script/sh/_command/do
* /tmp/work/RaspberryPi.Home.Root.20180318143826/src/script/sh/_command/do

```sh
#!/bin/bash
# やってみるコマンド。単一ファイルを/tmp/work/flow/do/に配置する
# $1: ext (.py, .sh, .md, .html, .js, .cs, ...)
# $2..: context (cui, gui, http, server)
#       template-vars (テンプレ変数)

[ $# -lt 1 ] && { echo "引数不足です。ファイル拡張子をください。"; exit 1; }

# jinja2がある仮想環境を有効化
. ~/root/script/sh/pyenv.sh
. ~/root/env/py/template/bin/activate

# テンプレファイルを作成する
pyscript="/tmp/work/Python.TemplateFileMaker.20180314204216/src/do.py"
#pyscript="~/root/script/py/_command/do/do.py"
filepath=`python3 "${pyscript}" "$@"`

# 成功すればエディタで開く
if [ -f "$filepath" ]; then
    [ -z "$editor" ] && [ "${editor:-A}" = "${editor-A}" ] && editor='vim'
    "$editor" "$filepath"
else
    # 失敗ならエラーを表示する（テンプレ変数の説明等）
    echo "$filepath"
fi
```

## 名前

ファイル、ディレクトリ、セクション、キー、変数などの名前をどうするか。

### 複数形

複数形は使わない。`templates`にすべきと思ったが、`command`も`commands`にしなければならない。libもlibrariesに, `script`も`scripts`にせねば。むしろ、すべて複数形ではないか？ 

複数形にすると統一性が保てなくなる。s, esなどもそうだし、indexはindicesになる。もはや元型が崩れる。悩むので使わない。

でも、`root.ini`のセクション名は`Paths`とする。`Path`は既存の環境変数名とかぶるから。shell文脈の都合により、統一できない。

### erとor

creater, creator, で悩む。前者は英語、後者は米語らしいが、単語によって変わったりもするらしい。統一性が保てない。すでに`NameGenerator`などで使ってしまった。

クラス名やモジュール名ではよく使う。`er`, `or`をやめた名詞にすべき？`NameGenerator`は`Name`と`Generate()`にすれば解決する、か？ `NameSequencer.Generate()`とかにしたくなる。ただの名前でなくて連番名なので`SequenceName.Generate()`がいいか？

http://tak-shonai.cocolog-nifty.com/crack/2013/09/-er--or-b920.html

### 大文字と小文字

* Linux FileSystem
    * 区別する。設定で区別しないようにもできると思う
* Ini (Pythonのconfigparser)
    * Section: 区別する
    * Key: 区別しない

統一できない。

# TSVファイルの必要性

## commands.tsv

テンプレートファイルをすべて捜査する回数を減らせる。

RAMディスクに配置したら、doコマンド初回利用時にのみ実行される。
ファイルがなければ、doコマンドでTABキー2回押下するたびに、テンプレートファイルをすべて探さねばならない。コマンド文字列の作成も。

## command_replace.tsv

冗長なコマンドを置き換える。

ファイルの分類を最適化するためにディレクトリ構造やファイル名を定める。だが、コマンド入力時、その構造そのままだと都合が悪いことがある。冗長など。

