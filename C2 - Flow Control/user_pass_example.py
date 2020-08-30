while True:
    print('Please type in your username below:')
    name = input()
    if name != 'Johnny':
        continue
    print('Please type in your password below:')
    password = input()
    if password == 'password':
        break
    else:
        print('That username or password is incorrect. Please try again.')
print('Access granted.')
