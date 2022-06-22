# 1
# Write a Python function called max_num()to find the maximum of three numbers.
from operator import truediv


def max_num(*args):
    answer = float('-inf')
    for arg in args:
        if arg > answer:
            answer = arg
    return answer


print(max_num(1666666, 1, 4, 7, -58145, 2, 8, 1249))

# 2
# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(lst):
    total = 1
    for num in lst:
        total *= num
    return total


print(mult_list([1, 2, 3, 4, 5]))

# 3
# Write a Python function called rev_string() to reverse a string.


def rev_string(string):
    return string[::-1]


print(rev_string("Hello"))

# 4
# Write a Python function called num_within() to check whether a number falls in a given range.


def num_within(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False


print(num_within(10, 2, 5))

# 5
# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.


def pascal(n):
    if n == 0:
        return []
    answer = [[1]]
    for i in range(n-1):
        last_row = [0] + answer[-1] + [0]
        new_row = []
        for j in range(len(answer[-1]) + 1):
            new_row.append(last_row[j] + last_row[j+1])
        answer.append(new_row)
    return answer


print(pascal(6))
