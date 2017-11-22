number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print(number , ' = ', guess)
elif guess < number:
    print(guess , ' < ', number)
else:
    print(guess , ' > ', number)

print('Done')

if 1 == 1:
    print(' short')
