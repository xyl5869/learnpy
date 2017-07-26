#!/usr/bin/python
# encoding:utf8
# Author:Along
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is",ab['Swaroop'])
print("Larry's address is",ab['Larry'])

del ab['Spammer']
print('\nThere are {} contacts in address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is",ab['Guido'])

print(ab.items())