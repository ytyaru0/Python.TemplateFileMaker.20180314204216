print('*** 代数演算子 ***')
print(1 + 1)
print(10 - 1)
print(2 * 3)
print(10 / 3)
print(10 // 3) # 切り捨て
print(10 % 3) # 剰余
print(2 ** 8) # 冪乗

print('*** Bit演算子 ***')
a = 0b01
b = 0b10
print(f'{a:02b}, {b:02b}')
print(f'NOT {~a:02b}, {~b:02b}')
print(f'AND {a&b:02b}')
print(f'OR  {a|b:02b}')
print(f'XOR {a^b:02b}')
print(f'L   {a<<1:02b}')
print(f'R   {a>>1:02b}')

print('*** 代入演算子 ***')
a = 3; b = 7;
a += b; print(a); a = 3;
a -= b; print(a); a = 3;
a *= b; print(a); a = 3;
a /= b; print(a); a = 3;
a %= b; print(a); a = 3;
a **= b; print(a); a = 3;
a //= b; print(a); a = 3;
print('*** 代入演算子 Bit ***')
a = 0b01; b = 0b10;
a &= b; print(f'{a:02b}'); a = 0b01;
a |= b; print(f'{a:02b}'); a = 0b01;
a ^= b; print(f'{a:02b}'); a = 0b01;
a <<= 1; print(f'{a:02b}'); a = 0b01;
a >>= 1; print(f'{a:02b}'); a = 0b01;

print('*** 比較演算子 Bit ***')
print(1 == 1)
print(1 != 2)
print(1 < 2)
print(2 > 1)
print(1 <= 1)
print(1 >= 1)
print(1 is 1)
print(1 is not 2)
print(2 in [1,2,3])
print(4 not in [1,2,3])
a = [1,2]; b = [1,2];
print(a == b)
print(a is b)
print(id(a) == id(b))
print(isinstance(a, list))
print(isinstance(b, list))
print(issubclass(int, object))

print('*** 真偽演算子 ***')
print(True and True)
print(True or False)
print(not False)

print('*** 三項演算子 ***')
print(1 if True else 2)
print(1 if False else 2)

print('*** 文字列連結 ***')
print('A' 'B')
print('A' + 'B')
print('A' * 3)

