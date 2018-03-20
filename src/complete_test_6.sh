
# doコマンドのサブコマンド候補と入力補完をする
#   https://qiita.com/sosuke/items/06b64068155ae4f8a853
#   COMP_CWORD	補完対象の引数の番号
#   COMP_LINE	コマンドライン全体の文字
#   COMP_POINT	カーソルの位置
command=do
SetupComplete()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    case "$COMP_CWORD" in
    1) COMPREPLY=( $(compgen -W "py sh" -- $cur) );;
    2)
        case "${COMP_WORDS[$(( COMP_CWORD - 1 ))]}" in
        "py") COMPREPLY=( $(compgen -W "context syntax designpattern" -- $cur) );;
        "sh") COMPREPLY=( $(compgen -W "AA BB CC" -- $cur) );;
        esac;;
    3)
        case "${COMP_WORDS[$(( COMP_CWORD - 2 ))]}" in
        "py" )
            case "${COMP_WORDS[$(( COMP_CWORD - 1 ))]}" in
            "context" ) COMPREPLY=( $(compgen -W "db http ui server" -- $cur) );;
            "syntax" ) COMPREPLY=( $(compgen -W "if for slice class" -- $cur) );;
            "designpattern" ) COMPREPLY=( $(compgen -W "singleton" -- $cur) );;
            esac;;
        "sh" )
            case "${COMP_WORDS[$(( COMP_CWORD - 1 ))]}" in
            "syntax" ) COMPREPLY=( $(compgen -W "if for function" -- $cur) );;
            esac;;
        esac;;
    esac
}
complete -F SetupComplete $command
