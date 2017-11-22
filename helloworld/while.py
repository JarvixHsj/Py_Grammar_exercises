number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print(guess,' == ' , number)
        running = False
    elif guess < number :
        print(guess,' < ' , number)
    else:
        print(guess,' > ' , number)
else:
    print('game over.')

print('Done')
