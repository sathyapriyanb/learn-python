inp_list = [int(x) for x in input()]
print([sum(inp_list[:i + 1]) for i in range(len(inp_list))])