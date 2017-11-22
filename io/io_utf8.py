# encoding=utf-8
__anthor__ = 'Jarvix'

import io

f = io.open('abc.txt', 'wt',encoding="utf-8")
f.write(u"Imagine non-ENglish language here")
f.close()

text = io.open('abc.txt', encoding="utf-8").read()
print(text)

