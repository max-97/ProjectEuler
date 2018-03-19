import time

sequence = {1: 1}
t1 = time.time()
for start in range(2, 1000000):
    i = start
    count = 0
    while i not in sequence.keys():
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3 * i + 1
        count += 1
    sequence[start] = count + sequence[i]

t2 = time.time()
print(t2-t1)
longest_sequence = 0
length = 0
for k, v in sequence.items():
    if v > length:
        longest_sequence = k
        length = v


print(longest_sequence)
