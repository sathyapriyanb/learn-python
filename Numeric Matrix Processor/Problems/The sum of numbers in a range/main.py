def range_sum(numbers, start, end):
    return sum(i for i in numbers if start <= i <= end)


input_numbers = [int(i) for i in input().split()]
a, b = input().split()
print(range_sum(input_numbers, int(a), int(b)))
