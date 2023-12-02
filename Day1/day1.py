import re
values = []
with open("input.txt") as file:
    for line in file:
        values.append(line.rstrip())
sum = 0
for line in values:
    digits_only = re.sub('\D','',line)
    sum += int(digits_only[0] + digits_only[-1])
print(sum)