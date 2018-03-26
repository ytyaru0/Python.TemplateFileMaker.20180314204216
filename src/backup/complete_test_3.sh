#!/bin/bash
# $ . <this-file>
# $ chrome [TAB]
_chrome()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    #COMPREPLY=( $(compgen -W "standard beta dev canary" -- $cur) )
    echo $COMP_CWORD
    case "$COMP_CWORD" in
        1) COMPREPLY=( $(compgen -W "standard beta dev canary" -- $cur) );;
        *) COMPREPLY=( $(compgen -W "$(ls)" -- $cur) );;
    esac
}

complete -F _chrome chrome
