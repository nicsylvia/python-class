# 2. Create a function that will sum all the numbers from a lower limit to an upper limit as seen on
# number 3 on assignment 2

def Total(lower, upper):
    while lower <= upper:
        upper += lower
        lower += 1
    print(upper)

Total(1, 4)