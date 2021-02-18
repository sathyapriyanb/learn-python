# write your code here
with open('salary.txt') as f, open('salary_year.txt', 'w') as f2:
    for line in f:
        f2.write(str(int(line) * 12) + '\n')
