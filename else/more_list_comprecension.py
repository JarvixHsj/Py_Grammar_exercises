# -*- coding:utf-8 -*-
__anthor__ = 'Jarvix'
# 判断已有数组中的值，当值大于2则乘2.
listone = [2,3,4]
listtow = [2*i for i in listone if i > 2]
print(listtow)
