
import pandas as pd
from typing import Union, Optional, Dict, Any
import pprint

print('\nbook chapter 6')
print('\nModifying Values in a Dictionary (book-95)')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
# This must be a fast alien. 
    x_increment = 3 
# The new position is the old position plus the increment.
#alien_0['x_position'] = alien_0['x_position'] + x_increment  (write easy code)

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

print('\nspeed = fast (book-95)')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
# This must be a fast alien. 
    x_increment = 3 
# The new position is the old position plus the increment.
#alien_0['x_position'] = alien_0['x_position'] + x_increment  (write easy code)

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

print('\nLoop inside Loop (book 97, 102)')
print('A Dictionary of Similar Objects (book-97)')
favorite_languages = { 'jen': 'python',
                        'sarah': 'c', 
                        'edward': 'rust', 
                        'phil': 'python', }

language = favorite_languages['sarah'].title()      # Sarah's favorite language is C.
print(f"Sarah's favorite language is {language}.")

print('\nLooping Through All the Keys in a Dictionary (book 102) 1:18')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title() 
        print(f"\t{name.title()}, I see you love {language}!")

print('erin' not in favorite_languages.keys())
print("Erin, please take our poll!")

if 'erin' not in favorite_languages.keys(): 
    print("Erin, please take our poll!")

print('\nin oprator: search substring')
print( "SerachGame" in '''Hi do you now where is SerachGame, find out somewhere ''')

print("Qasim" in """My Name is Muhammad Qasim, I'm working as Chief Data Scientist!""")

print('\nA List of Dictionaries [multiple dictionaries in a lis] (book 105)')

Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

alien_0 : list[Key,Value]  = {'color': 'green', 'points': 5} 
alien_1 : list[Key,Value]  = {'color': 'yellow', 'points': 10} 
alien_2 : list[Key,Value]  = {'color': 'red', 'points': 15}

aliens : list[Dict[str,str]] = [alien_0, alien_1, alien_2]    # put all three objects in list here

for alien in aliens:
    print(alien)

print('\n (book 105)')
# Make an empty list for storing aliens.
aliens : list[Dict[str,str]] = []
import pprint
print(f'empty  {aliens}')       # empty
# Make 10 green aliens.
for alien_number in range(5):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
pprint.pprint(aliens)

# see only 2 values through slicing
print('apply slicing')
pprint.pprint(aliens[:2])

# update the value of first 2
print('Update')
for alien in aliens[:2]:        # update top 2
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

pprint.pprint(aliens[:4])

print('update')
for alien in aliens[0:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

pprint.pprint(aliens[:5])