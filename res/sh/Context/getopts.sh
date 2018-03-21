# ./getopts.sh -a -b 1
while getopts ab: OPT; do
    case $OPT in
        "a" ) FLG_A="TRUE" ;;
        "b" ) FLG_B="TRUE" ; VALUE_B="$OPTARG" ;;
    esac
done
echo FLG_A=$FLG_A
echo FLG_B=$FLG_B
echo VALUE_B=$VALUE_B
