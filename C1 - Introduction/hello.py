# This program says hello and asks for a user's name and age.

print('Hello world!')
print('What is your name?') # ask for their name
myName = input()

print('It is nice to meet you ' + myName)
print('Bot has noticed that your name contains: ')
print(str(len(myName)) + ' characters')

print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 10) + ' in 10 years time.') # str(int(...)) is
# used in this context to first convert input to integer, add 10, then finally
# convert everything back to a string to be printed
