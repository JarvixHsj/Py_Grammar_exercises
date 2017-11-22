ab = {
    'Swaroop' : 'swaroop@swaroopch.com',
    'Larrt' : 'larrt@wall.org',
    'Matsumoto' : 'mate@ruby-lang.org',
    'Spammer' : 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])

#   删除一对键值
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'. format(name,address))

#添加一堆键值
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGudio's address is", ab['Guido'])


