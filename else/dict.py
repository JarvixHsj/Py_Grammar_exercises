# -*- coding:utf-8 -*-
__anthor__ = 'Jarvix'

# help(pow)
# exit()

def powersum(power, *args):
    '''Return the sum of each argument raised to te specified power.'''
    print('below is ',power,args)
    total = 0
    for i in args:
        print(pow(i, power))
        total += pow(i, power)
    return total

res = powersum(2,3,4)
print(res)
res2 = powersum(2,10)
print(res2)
