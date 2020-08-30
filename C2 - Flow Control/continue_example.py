spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # 'continue' forces the program to skip the step pertaining to
        # spam = 3
    print('spam is ' + str(spam))
