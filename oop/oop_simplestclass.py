class Person:
    pass #一个空的代码块


class Person2:
    def say_hi(self, name = 'Jarvix'):
        print('hi {0},how are you?'.format(name))

p = Person();
print(p)

print('-------Person2---------')

p2 = Person2()
p2.say_hi('hsj')
