# Simple program prints numbers 1 to 10 using for and while loop

print('For loop:')
for num in range(1, 11):
    print(num)

num = 0
print('While loop:')
while True:
    num = num + 1
    print(num)
    if num == 10:
        break
