{% import "md/meta_yaml_blog.md" as meta %}
{{ meta.put(Title=Title, Author='ytyaru', Date=Date, CSS='index.css') }}

{{ Desctiption }}

<!-- more -->

# 成果物

[{{ RepoUrl }}:embed]

## 開発環境

{% include "md/env/" + e + ".md" %}

## ライセンス

{% include "md/license/" + l + ".md" %}

