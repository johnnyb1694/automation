# This program contains a series of if/elif conditions

name = 'Dracula'
age = 110
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# Remember that the order of elif statements is important, because when using
# elif statements, once a condition is found to be true the remaining conditions
# are not tested
