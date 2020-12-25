number_of_halls, capacity, number_of_viewers = [abs(int(input())) for _ in range(3)]
print(number_of_viewers <= number_of_halls * capacity)
