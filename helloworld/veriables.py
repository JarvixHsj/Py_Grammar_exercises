#-------变量-----------
i = 5
print(i)
i = i + 1 #运算顺序，先将 i 赋值给 i ，原本i=5 则变成 5 = 5 + 1 再算后面的 + ，算完再更新内存的i
print(i)

s = '''This is muiti-line string.
This is the second line.'''
print(s)
# 代码换行，但是输出结果不换行
ss = 'This is line is auto huanhang .\
This is two line.'
print(ss)

print(3**4)  # 相当于 3 * 3 * 3 * 3
print(13/3)
print(13//3)    #整除，取整至接近整数
print(13%3)     #取模，返回算法运算后的余数
print(11<<1)    #左移， 11的二进制是 1011，向左移一位，则末尾加0 变成10110
print(21>>2)    #右移， 11的二进制是 10101，向右移两位，则从左往右推掉两位，变成101

print(5 & 3)    #按位与，都转换成二进制，然后对比，都为1，则为1，否则为0
print(5 | 3)    #按位或，都转换成二进制，然后对比，其中一个为1，则为1，否则为0
print(5 ^ 3)    #按位异或，都转换成二进制，然后对比，其中一个为1，另一个为0，则为1，否则为0
