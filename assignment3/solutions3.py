# 3. Create a function in Python that will determine average of any numbers in a Python list.

list = [3, 4, 5, 6, 7]


def Average(numbers):
    sum = 0
    for numbers in list:
        sum += numbers
        average = sum/len(list)
    print(average)
list = [3, 4, 5, 6, 7]
Average(list)