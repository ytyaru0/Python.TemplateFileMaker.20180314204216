class TemplateReplacer:
    def Replace():
        


if __name__ == '__main__':
    # $1: 置換するファイルパス
    # $2..: テンプレート変数を置換するための引数
    #   位置引数: ${0}, ${1}, などのテンプレート引数に対応する
    #   キーワード引数: ${Name}などの名前付きテンプレート引数に対応する
    

    import sys
    import os.path
    from CommandsFile import CommandsFile
    input_command = ' '.join([a for a in sys.argv[1:]]).strip()
    f = CommandsFile()
    #print(input_command)
    for d in f.Load():
        for c in d.commands:
            #print('*'+c)
            if c == input_command:
                print(os.path.join(f.TemplateDir, d.path))
                sys.exit()
    raise Exception('<ERROR> 指定したコマンドに該当するテンプレートファイルパスは存在しません。')

