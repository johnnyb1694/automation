# This prints 'Hello' if 1 is stored in spam and prints 'Howdy' elsewhere

print('Please input a value for spam: ')
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
