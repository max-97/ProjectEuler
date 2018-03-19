import datetime

num_sundays = 0

# for j in range(1901, 2001):
#     for m in range(1, 13):
#         if datetime.date(j, m, 1).weekday() == 6:
#             num_sundays += 1
#

num_sundays = sum([1 for j in range(1901, 2001) for m in range(1, 13) if datetime.date(j, m, 1).weekday() == 6])

print(num_sundays)
