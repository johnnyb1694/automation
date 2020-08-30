import sys


def collatz(number):

    try:
        value = int(number) % 2

        if value == 0:
            return_0 = int(number) // 2
            print(str(return_0))
            return(return_0)

        else:
            return_1 = int(number) * 3 + 1
            print(str(return_1))
            return(return_1)

    except ValueError:
        print('Error: you must enter a positive integer!')
        sys.exit()


print('Please choose a number: ')
chosen_number = input()

current_seq_val = collatz(chosen_number)
while current_seq_val != 1:
    current_seq_val = collatz(current_seq_val)
