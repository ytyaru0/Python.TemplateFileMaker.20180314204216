import pathlib
import shlex
import jinja2
from jinja2 import Template, Environment, FileSystemLoader, meta
from CommandsFile import CommandsFile

class CopyTemplate:
    def __init__(self, commands:list, filepath:str):
        self.__commands = commands
        self.__filepath = filepath
        self.__cmdfile = CommandsFile()
        self.__tpl_var_prefix = '-'

    def Copy(self):
        with open(self.__filepath, 'w') as f:
            f.write(self.__CommandToTemplate())

    def __CommandToTemplate(self):
        categolies, tpl_var_dict = TemplateVarsArgumentAnalizer(self.__tpl_var_prefix).Analize(self.__commands)
        path = self.__CommandToTemplatePath(categolies)
        env = Environment(loader=FileSystemLoader(str(self.__cmdfile.TemplateDir)))
        template = env.get_template(path)
        try:
            return template.render(**tpl_var_dict)
        except jinja2.exceptions.UndefinedError as e:
            import traceback
            traceback.print_exc()
            self.__GetIncludeFilesCandidateMessage(categolies, env, template)
            sys.exit(1)

    def __CommandToTemplatePath(self, categolies:list):
        input_command = ' '.join([a for a in categolies]).strip()
        for d in self.__cmdfile.Load():
            for c in d.commands:
                if c == input_command:
                    return d.path
        raise Exception('コマンドに対応するテンプレートファイルパスが見つかりません。\n  command=\'{}\'\n  参照ファイル:{}'.format(' '.join(self.__commands), self.__cmdfile.FilePath))

    def __GetIncludeFilesCandidateMessage(self, categolies:list, env:jinja2.Environment, template:jinja2.Template):
        with pathlib.Path(template.filename).open() as f:
            source = f.read()
            includes = TemplateIncludeFiles(self.__cmdfile.TemplateDir, env).Get(source)
            print('テンプレート変数が不足しています。')
            print('たとえば以下のように入力してください。')
            tpl_var_names = sorted(meta.find_undeclared_variables(env.parse(source)), key=str.lower)
            print('$ do', ' '.join(categolies), self.__GetExampleCommand(tpl_var_names, includes))
            print('テンプレート変数は以下のコマンドで指定します。')
            print(' '.join([self.__tpl_var_prefix + v for v in tpl_var_names ]))
            if 0 < len(includes):
                print('include用テンプレ引数とその値の候補は以下のとおり。')
                for i in includes:
                    print(self.__tpl_var_prefix+i[0], i[1])
            print('対象テンプレートは以下です。')
            print(template.filename)

    def __GetExampleCommand(self, tpl_var_names, includes):
        command = ''
        inc_names = [i[0] for i in includes]
        for n in tpl_var_names:
            if n in inc_names: continue
            command += self.__tpl_var_prefix + n + ' A '
        for i in includes:
            command += self.__tpl_var_prefix + i[0] + ' ' + i[1][0] + ' '
        return command
        
# -V -V -V
# -" -V" -V
# -K V -K V
# -K "-V" -K V
# -V -V -V -K V -V -K V
# Key: -[_a-zA-Z][_a-zA-Z0-9]。テンプレ変数名と同一。重複したら後者で上書き。
# Value: スペースやハイフンを使うときはクォーテーションで囲む。
class TemplateVarsArgumentAnalizer:
    def __init__(self, tpl_var_prefix):
        self.__tpl_var_prefix = tpl_var_prefix
    @property
    def Prefix(self): return self.__tpl_var_prefix

    # tpl_vars: shlex.split()済みで先頭に`-`がある要素以降すべて
    def Analize(self, commands:list):
        categolies, tpl_vars = self.__SplitCategolyAndTemplateVars(commands)
        return categolies, self.__MakeTemplateVarsDict(tpl_vars)

    # コマンド文字列をカテゴリとテンプレ変数に分離する
    # command: $ do {categoly} ... -{tpl_var} ... 
    def __SplitCategolyAndTemplateVars(self, commands:list):
        for i, a in enumerate(commands):
            if a.startswith(self.Prefix): return commands[:i], commands[i:]
        return commands, []

    def __MakeTemplateVarsDict(self, tpl_vars):
        tpl_var_dict = {}
        position = 0 # 位置引数カウンタ
        for i, v in enumerate(tpl_vars):
            if self.IsPositional(tpl_vars, i):
                tpl_var_dict[str(i)] = self.UnQuote(v[1:])
                position += 1
            else:
                if not self.IsLast(tpl_vars, i):
                    tpl_var_dict[v[1:]] = self.UnQuote(tpl_vars[i+1])
        return tpl_var_dict

    def IsPrefix(self, arg): return arg.startswith(self.Prefix)
    def IsLiteral(self, arg):
        if arg.startswith('\'') and arg.endswith('\''): return True
        elif arg.startswith('"') and arg.endswith('"'): return True
        else: return False
    def UnQuote(self, arg):
        if self.IsLiteral(arg): return arg[1:-1].replace('\\', '')
        else: return arg
    def IsPositional(self, tpl_vars:list, start:int):
        if self.IsLast(tpl_vars, start): return self.IsPrefix(tpl_vars[start])
        if self.IsPrefix(tpl_vars[start]) and self.IsPrefix(tpl_vars[start+1]):
            return True
        return False
    def IsLast(self, tpl_vars:list, index:int):
        if index+1 == len(tpl_vars): return True
        else: return False

class TemplateIncludeFiles:
    def __init__(self, tpl_dir:pathlib.Path, env:jinja2.Environment):
        self.__tpl_dir = tpl_dir
        self.__env = env

    def Get(self, source:str):
        token_gen = self.__env.lex(self.__env.preprocess(source))
        tokens = list(token_gen)
        return sorted(self.GetIncludeCandidates(tokens, self.GetBlockContentIndices(tokens)), key=lambda i: i[0].lower())
           
    def GetBlockContentIndices(self, tokens):
        block_indices = []
        start = -1
        for i, t in enumerate(tokens):
            if -1 != start:
                if t[1] == 'block_end':
                    block_indices[-1][1] = i
                    start = -1
                    continue
            else:
                if t[1] == 'block_begin':
                    start = i 
                    block_indices.append([start, -1])
                    continue
        return block_indices

    def GetIncludeCandidates(self, tokens, block_indices):
        values = []
        for rng in block_indices:
            start = rng[0] + self.GetIncludeValueInde(tokens[rng[0]:rng[1]])
            if -1 == start: continue
            values.append(self.GetIncludeValuePattern(tokens[start+1:rng[1]-1]))
        return values

    def GetIncludeValueInde(self, block_tokens):
        for i, token in enumerate(block_tokens):
            if token[1] == 'name':
                # {% block で見つかった最初の name構文 の値が include なら真
                if token[2] == 'include': return i
                # {% block では 変数なども name構文である。includeという名の変数もありうるが、最初にきているかどうかで変数かどうか判断できる
                else: return -1
        return -1

    def GetIncludeValuePattern(self, include_value_tokens:list):
        name = None
        value = ''
        for i, token in enumerate(include_value_tokens):
            if 'string' == token[1]: value += token[2][1:-1]
            elif 'name' == token[1]:
                if name is None:
                    name = token[2]
                    value += '**/*'
                else: raise Exception('includeブロック {% include %} の値に2つ以上の テンプレ変数 {{}} を使っています。ひとつだけにしてください。')
        return name, self.__GetPatternValues(value)

    def __GetPatternValues(self, pattern):
        pattern_parent = pathlib.PurePath(pattern).parent.parent
        pattern_full = self.__tpl_dir / pattern_parent
        values = []
        for path in self.__tpl_dir.glob(pattern):
            p = path.relative_to(pattern_full)
            values.append(str(p.parent / p.stem))
        return sorted(values, key=str.lower)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3: raise Exception('起動引数エラー。コマンド文字列と出力先ファイルのフルパスをください。')
    c = CopyTemplate(sys.argv[1:-1], sys.argv[-1])
    c.Copy()
