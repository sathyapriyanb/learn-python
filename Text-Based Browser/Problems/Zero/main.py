n = int(input())
denominator = int(input())
try:
    n_denominator = n // denominator
except ZeroDivisionError:
    print('Division by zero is not supported')
else:
    print(n_denominator)