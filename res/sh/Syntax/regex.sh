name='name.sh'
if [[ $name =~ .sh ]]; then
    echo IN
fi

name='2000/01/01'
if [[ $name =~ [0-9]{4}/[0-9]{2}/[0-9]{2} ]]; then
    echo IN
fi

pattern='[0-9]{4}/[0-9]{2}/[0-9]{2}'
if [[ $name =~ $pattern ]]; then
    echo IN
fi

res=`echo -e 'A\nB\nAB\nab' | grep 'A'`
echo $res
res=`echo -e 'A\nB\nAB\nab' | grep -i 'a'`
echo $res

