#!/bin/bash

# $ . <this-file>
# $ chrome [TAB]
_chrome()
{
      COMPREPLY=( standard beta dev canary )
}

complete -F _chrome chrome
