# 構造

* ~/root/script/
    * sh/
        * _command/
            * do
    * py/
        * os/file/
        * _command/
            * do/
                * CommandReplaceFile.py
                * CommandsFile.py
                * GetCompleteCandidate.py
                * GetTemplateFilePath.py
                * PathToCommand.py
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

