
x = 2*2*2*2*3*3*5*7*11*13*17*19


def is_divisible(j):
    for i in range(1, 21):
        if j % i != 0:
            return True
    return False


while is_divisible(x):
    x += 1


print(x)
