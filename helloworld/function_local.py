x = 50
y = 20
def func(x):
    global y
    print('y is', y)
    y = 19
    print('x is ', x)
    x = 2
    print('change local x to ', x)

func(x)

print('x is still', x)
print('y is', y)
