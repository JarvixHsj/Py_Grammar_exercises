import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe python path is ', sys.path, '\n')

from math import  sqrt
print("square root of 16 is ", sqrt(16))
print(__name__)

print(dir(sys))
