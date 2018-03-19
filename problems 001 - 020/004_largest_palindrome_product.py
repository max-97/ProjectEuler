def is_palindrome(product):
    num_list = [int(d) for d in str(product)]
    for i in range(len(num_list)):
        if num_list[i] != num_list[-i - 1]:
            return False
    return True


def largest_prime_product():
    pal = []
    for i in range(999, 899, -1):
        for j in range(i, 899, -1):
            if is_palindrome(i * j):
                pal.append(i * j)
    return pal


print(max(largest_prime_product()))
