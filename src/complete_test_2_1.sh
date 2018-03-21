#!/bin/bash

# $ . <this-file>
# $ chrome [TAB]
_chrome()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    local candidate="standard beta dev canary"
    COMPREPLY=( $(compgen -W "$candidate" -- $cur) )
}

complete -F _chrome chrome
