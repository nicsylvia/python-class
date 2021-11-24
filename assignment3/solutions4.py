# 4. Create a python function that sums all the numbers from a lower value to an upper value.


def sum(lower, upper):
    lower = 1
    total = 0
    while lower <= upper:
        total +=  lower
        lower += 1
    print(total)

sum(1, 30)