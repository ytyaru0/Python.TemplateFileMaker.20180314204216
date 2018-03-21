
# doコマンドのサブコマンド候補と入力補完をする
#   https://qiita.com/sosuke/items/06b64068155ae4f8a853
#   COMP_CWORD	補完対象の引数の番号
#   COMP_LINE	コマンドライン全体の文字
#   COMP_POINT	カーソルの位置
command=do
SetupComplete()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    #pyscript="/tmp/work/Python.TemplateFileMaker.20180314204216/src/GetCompleteCandidate.py"
    echo "ECHO CWORD: $COMP_CWORD"
    echo "ECHO LINE: $COMP_LINE"
    echo "ECHO POINT: $COMP_POINT"
    #candidate="$(python3 "$pyscript" "$command" "$COMP_CWORD" "$COMP_LINE" "$COMP_POINT")"
    #echo "candidate = $candidate"
    #COMPREPLY=( $(compgen -W "$candidate" -- $cur) )
    COMPREPLY=( $(compgen -W "standard beta dev canary" -- $cur) )
    #COMPREPLY=( $(compgen -W "${candidate}" -- $cur) )
}
complete -F SetupComplete $command
