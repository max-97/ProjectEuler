
solution = 1000
for a in range(1, 334):
    for b in range(a + 1, 500):
        c = solution - a - b
        if a**2 + b**2 == c**2:
            print(str(a) + " " + str(b) + " " + str(c))
            print(a*b*c)
            break
