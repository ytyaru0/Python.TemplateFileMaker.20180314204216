# 数値
test 1 -eq 1; echo $?
test 1 -ne 2; echo $?
test 1 -lt 2; echo $?
test 2 -gt 1; echo $?
test 1 -le 1; echo $?
test 1 -ge 1; echo $?
# AND, OR
test 1 -eq 1 -a 2 -eq 2; echo $?
test 1 -eq 2 -o 2 -eq 2; echo $?
test \( 1 -eq 2 -o 2 -eq 2 \) -a 3 -eq 3; echo $?
( [ 1 -eq 2 ] || [ 2 -eq 2 ] ) && [ 3 -eq 3 ]; echo $?
if ( [ 1 -eq 2 ] || [ 2 -eq 2 ] ) && [ 3 -eq 3 ]; then
    echo $?
fi
# 文字列
test 'A' == 'A'; echo $?
test 'A' != 'B'; echo $?
# ファイル更新日時
NEW=/tmp/work/new.txt
OLD=/tmp/work/old.txt
touch -d "1999/12/31 23:59:59" $OLD
touch -d "2000/01/01 00:00:00" $NEW
test $NEW -nt $OLD; echo $?
test $OLD -ot $NEW; echo $?
[ $NEW -nt $OLD ]; echo $?
[ $OLD -ot $NEW ]; echo $?
test -z ""; echo $?
test -n "A"; echo $?
test -d $(dirname $NEW); echo $?
test -f $NEW; echo $?
echo 'A' > $NEW
test -s $NEW; echo $?
test -e $NEW; echo $?
chmod 755 $NEW
test -r $NEW; echo $?
test -w $NEW; echo $?
test -x $NEW; echo $?

