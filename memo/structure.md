# 構造

* ~/.bashrc
    * python3 ~/root/script/_meta/path/IniToSh.py
    * . ~/root/script/_meta/path/sh/paths.sh
    * . setup_complete_candidate_do.sh
* ~/root/script/
    * _meta/
        * path/
            * ini/
                * root.ini
                * work.ini
            * sh/
                * paths.sh
            * IniToSh.py
        * command/
            * setup_complete_candidate_do.sh
            * setup_complete_candidate_pj.sh
            * setup_complete_candidate_repo.sh
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
                    * GetCompleteCandidate.py
                    * GetTemplateFilePath.py
                    * PathToCommand.py
                    * config/
                        * command_replace.tsv
            * pj/
            * repo/

* ~/root/db/
    * templates/
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

