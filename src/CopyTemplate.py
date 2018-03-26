import pathlib
import shlex
from jinja2 import Template, Environment, FileSystemLoader, meta
from CommandsFile import CommandsFile

class CopyTemplate:
    def __init__(self, commands:list, filepath:str):
        self.__commands = commands
        self.__filepath = filepath
        self.__cmdfile = CommandsFile()

    def Copy(self):
        with open(self.__filepath, 'w') as f:
            f.write(self.__CommandToTemplate())

    def __CommandToTemplate(self):
        categolies, tpl_var_dict = TemplateVarsArgumentAnalizer().Analize(self.__commands)
        path = self.__CommandToTemplatePath(categolies)
        print(str(self.__cmdfile.TemplateDir))
        print(path)
        env = Environment(loader=FileSystemLoader(str(self.__cmdfile.TemplateDir)))
        template = env.get_template(path)
        return template.render(**tpl_var_dict)

    def __CommandToTemplatePath(self, categolies:list):
        input_command = ' '.join([a for a in categolies]).strip()
        for d in self.__cmdfile.Load():
            for c in d.commands:
                if c == input_command:
                    return d.path
        raise Exception('コマンドに対応するテンプレートファイルパスが見つかりません。\n  command=\'{}\'\n  参照ファイル:{}'.format(' '.join(self.__commands), self.__cmdfile.FilePath))

    def GetTemplateVars(self):
        categolies, tpl_var_dict = TemplateVarsArgumentAnalizer().Analize(self.__commands)
        path = self.__CommandToTemplatePath(categolies)
        env = Environment(loader=FileSystemLoader(str(self.__cmdfile.TemplateDir)))
        template = env.get_template(path)
        with pathlib.Path(template.filename).open() as f:
             
            #msg = TemplateErrorMessage(env)
            #print(msg.Get(f.read()))
            #includes = TemplateIncludeFiles(env).Get(f.read())
            includes = TemplateIncludeFiles(self.__cmdfile.TemplateDir, env).Get(f.read())
            print('INCLUDES:', includes)

            ast = env.parse(f.read())
            return meta.find_undeclared_variables(ast)

# -V -V -V
# -" -V" -V
# -K V -K V
# -K "-V" -K V
# -V -V -V -K V -V -K V
# Key: -[_a-zA-Z][_a-zA-Z0-9]。テンプレ変数名と同一。重複したら後者で上書き。
# Value: スペースやハイフンを使うときはクォーテーションで囲む。
class TemplateVarsArgumentAnalizer:
    def __init__(self): pass

    @property
    def Prefix(self): return '-'

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

import jinja2
class TemplateIncludeFiles:
    def __init__(self, tpl_dir:pathlib.Path, env:jinja2.Environment):
        self.__tpl_dir = tpl_dir
        self.__env = env

    def Get(self, source:str):
        token_gen = self.__env.lex(self.__env.preprocess(source))
        tokens = list(token_gen)
        return self.GetIncludeCandidates(tokens, self.GetBlockContentIndices(tokens))
           
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
        print(block_indices)
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
        return values


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3: raise Exception('起動引数エラー。コマンド文字列と出力先ファイルのフルパスをください。')
    c = CopyTemplate(sys.argv[1:-1], sys.argv[-1])
    try:
        c.Copy()
        print(c.GetTemplateVars())
    except:
        import traceback
        traceback.print_exec()

