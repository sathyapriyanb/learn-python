def last_indexof_max(numbers):
    # write the modified algorithm here
    return len(numbers) - numbers[::-1].index(max(numbers)) - 1
