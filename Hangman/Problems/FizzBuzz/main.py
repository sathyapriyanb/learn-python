for i in range(1, 101):
    if all([i % 3 == 0, i % 5 == 0]):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
