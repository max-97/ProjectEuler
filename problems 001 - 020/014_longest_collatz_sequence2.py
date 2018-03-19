import time

sequence = {1: 1}


def calculate_collatz(n):
    if n not in sequence.keys():
        if n % 2 == 0:
            sequence[n] = calculate_collatz(n / 2) + 1
        else:
            sequence[n] = calculate_collatz(3 * n + 1) + 1
    return sequence[n]


t1 = time.time()

for start in range(2, 1000000):
    calculate_collatz(start)

t2 = time.time()
print(t2-t1)

print(max(sequence, key=sequence.get))
