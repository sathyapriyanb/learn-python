# use the function blackbox(lst) that is already defined
lst = [1, 2]
new_lst = blackbox(lst)
print(*["modifies" if new_lst is lst else "new"])