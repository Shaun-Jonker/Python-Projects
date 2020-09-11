import re

file = open("regex_sum.txt")
num_list = []

for line in file:
    if re.findall('[0-9]+', line):
        num_list.append(re.findall('[0-9]+', line))

total = 0
for line in num_list:
    for num in line:
        total += int(num)

print(total)

print(sum([n for n in re.findall('[0-9]+', file.read())]))

file.close()
