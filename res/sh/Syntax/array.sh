array=(A B C)
echo num=${#array[@]}
for i in ${array[@]}; do
    echo $i
done

declare -A Names
Names=(
    [A]=AA
    [B]=BB
)
echo num=${#Names[@]}
for key in ${!Names[@]}; do
    echo ${Names[$key]}
done

declare -A Names
Names=(
    ['C']='CC'
    ['D']='DD'
)
echo num=${#Names[@]}
for key in ${!Names[@]}; do
    echo ${Names[$key]}
done

