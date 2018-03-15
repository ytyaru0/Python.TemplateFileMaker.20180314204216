function A () {
    echo "$@"
}
A "$@"
ret=`A 1`
echo $ret

B () { echo 'B'; }
echo `B`
