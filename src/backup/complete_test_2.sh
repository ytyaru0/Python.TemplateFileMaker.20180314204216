#!/bin/bash

# $ . <this-file>
# $ chrome [TAB]
_chrome()
{
    local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -W "standard beta dev canary" -- $cur) )
}

complete -F _chrome chrome
