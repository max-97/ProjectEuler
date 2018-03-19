
numbers = [True] * 2000000
numbers[0] = False
numbers[1] = False

for i in range(len(numbers)):
    if numbers[i]:
        for x in range(2*i, 2000000, i):
            numbers[x] = False

sum = 0
for i, b in enumerate(numbers):
    if b:
        sum += i

print(sum)
