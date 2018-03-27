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


/tmp/work/.meta/_command/do/ 配下にコマンドファイルを作成する。
テンプレートファイルがあるディレクトリを捜査し、初回のみ作成する。
更新したいときはcommands.tsv、command_replace.tsvのファイルを削除すること。

なお、/tmp/はRAMディスクとする。
テンプレートが追加されるなどの変更があっても、tsvファイルの変更はメモリ上で保持される。SDカードやSSDへの書込は生じない。



と思ったが、command_replace.tsv は手書き。自動作成できない。
py/_command/do/ 配下にコードと一緒に配置するか。/tmp/work/.meta/ に存在しなければコピーして、そっちを読むようにする。

## 名前

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

# TSVファイル設定

config.ini

```ini
[file]
paths=
    /tmp/work/.meta/_command/do
    ./config
```

```python
import configparser
p = configparser.ConfigParser()
p.read('config.ini')
print(p['file']['paths'].split('\n'))

paths = filter(lambda line: line is not None and 0 < len(line.strip()), p['file']['paths'].split('\n')) 
print(list(paths))
```

config.yml

```yml
path:
    - /tmp/work/.meta/_command/do/
    - ./config/
```

