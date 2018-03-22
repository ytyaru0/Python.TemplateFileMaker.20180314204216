if __name__ == '__main__':
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

