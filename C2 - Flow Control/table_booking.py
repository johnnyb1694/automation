# An interesting feature of Python is that the following values are considered
# to be false:

# (int) 0
# (str) ''

# Therefore we can use this to create a simple program which registers guests

# User's name
name = ''
while not name:  # note that " '' " is false so " not '' " is true
    print('Please enter your name:')
    name = input()

# No. of people
print('How many people are in your party?')
peopleNo = int(input())
while not peopleNo:
    print('You cannot book a table for zero people!')
    print('Please re-enter how many people are in your party:')
    peopleNo = int(input())

# Time
print('What time would you like to book the table for?')
time = int(input())
while time > 8:
    print('Sorry there are no tables available during this time period.')
    print('Please choose another time:')
    time = int(input())
print('Thank you, ' + name + '. we will see you at ' + str(time) + 'pm this evening.')
