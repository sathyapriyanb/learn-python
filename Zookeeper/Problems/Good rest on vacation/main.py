# put your python code here
days, food_cost, flight_cost, hotel_cost = [abs(int(input())) for _ in range(4)]

print(food_cost * days + hotel_cost * (days - 1) + 2 * flight_cost)
