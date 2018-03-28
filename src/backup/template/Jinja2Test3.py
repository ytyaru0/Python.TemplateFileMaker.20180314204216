from jinja2 import Template, Environment, FileSystemLoader
import pathlib
import datetime

path_tpl = (pathlib.Path(__file__).parent.parent.parent.parent / 'res').resolve()
env = Environment(loader=FileSystemLoader(str(path_tpl )))
template = env.get_template('py/3/_MIN.py')
#template = env.get_template('md/artifact_1.md')
print(template.render(_0='MY_NAME'))
#print(template.render(**{'0': 'MY_NAME'}))
#print(template.render(Desctiption="説明文。", RepoUrl='http://', e='ras_py', l='CC0-1.0'))
"""
template = env.get_template('md/artifact_2.md')
template.globals['now'] = datetime.datetime.now()
print(template.render(Title='記事のタイトル', Desctiption="説明文。", RepoUrl='http://', e='ras_py', l='CC0-1.0'))
"""
"""
template = env.get_template('md/artifact_2.md')
print(template.render(Title='記事のタイトル', Date='{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), Desctiption="説明文。", RepoUrl='http://', e='ras_py', l='CC0-1.0'))
"""
