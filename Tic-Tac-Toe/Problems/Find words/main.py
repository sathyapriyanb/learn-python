input_list = input().split()
final_list = [input_string for input_string in input_list if input_string.endswith("s")]
print("_".join(final_list))
