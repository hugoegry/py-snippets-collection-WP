for i in range(-30, 30):
    if (i % 3) != 0 and (i % 5) != 0:
        print(i)
    if (i%3) == 0:
        print('Fizz', end='')
    if (i%5) == 0:
        print('Buzz')
