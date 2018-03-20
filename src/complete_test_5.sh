# doコマンドのサブコマンド候補と入力補完をする
#   https://qiita.com/sosuke/items/06b64068155ae4f8a853
#   COMP_CWORD	補完対象の引数の番号
#   COMP_LINE	コマンドライン全体の文字
#   COMP_POINT	カーソルの位置
# 確認方法
#   $ . <this-file>
#   $ do [TAB]
#   py sh
#   $ do py [TAB]
#   context syntax designpattern
command=do
SetupComplete()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    case "$COMP_CWORD" in
    1) COMPREPLY=( $(compgen -W "py sh" -- $cur) );;
    2)
        case "${COMP_WORDS[$(( COMP_CWORD - 1 ))]}" in
        "py" )
            COMPREPLY=( $(compgen -W "context syntax designpattern" -- $cur) );;
        "sh" )
            COMPREPLY=( $(compgen -W "AA BB CC" -- $cur) );;
        "*" )
            COMPREPLY=( $(compgen -W "$(ls)" -- $cur) );;
        esac
    esac
}

complete -F SetupComplete $command
