x = 600851475143
prime_factors = []


def is_prime(i):
    for j in range(2, i):
        if j in prime_factors and i % j == 0:
            break
    else:
        return i


i = 2

while i <= x:
    if x % i == 0:
        prime_factors.append(is_prime(i))
        x = x / i
        i = i - 1
    i = i + 1
print(prime_factors)
