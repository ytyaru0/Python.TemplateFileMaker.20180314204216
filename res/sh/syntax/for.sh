for i in `seq 0 3`; do
    echo $i
done

array=(A B C)
echo num=${#array[@]}
for i in ${array[@]}; do
    echo $i
done

declare -A Names
Names=(
    ['A']='AA'
    ['B']='BB'
)
echo num=${#Names[@]}
for key in ${!Names[@]}; do
    echo ${Names[$key]}
done



