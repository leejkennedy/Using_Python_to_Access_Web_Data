import re

with open("assignment.txt") as f:
    sum = 0
    match = re.findall(r"[\d]+", f.read())
    for num in match:
        sum += int(num)
    print(sum)
