[ 1 ] && echo 1
[ 1 ] && { echo -n 1; echo 2; }
[ 1 ] && [ 2 ] && { echo -n 1; echo 2; }
[ 1 ] || [ 2 ] && { echo -n 1; echo 2; }

if [ 1 ]; then
    echo 2
fi

if [ 1 -eq 2 ]; then
    echo 0
else
    echo 3
fi

if [ 1 -eq 2 ]; then
    echo 0
elif [ 1 ]; then
    echo 4
else
    echo 0 
fi

