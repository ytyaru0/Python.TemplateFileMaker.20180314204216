echo 'A,B,C,Dのいずれかを入力してください。'
read answer
case $answer in
    'A' ) echo A;;
    'B' ) echo B;;
    'C' | 'D' ) echo CorD;;
    * ) echo Other;;
esac

echo '何か一文字入力してください。'
read answer
case $answer in
    [a-z] ) echo 半角英字です。;;
    [A-Z] ) echo 全角英字です。;;
    [0-9] ) echo 数字です。;;
    * ) echo 知りません。;;
esac

