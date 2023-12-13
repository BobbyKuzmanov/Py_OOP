def number_increment(numbers):

    def increase():
        return [x + 1 for x in numbers]

    return increase()


print(number_increment([1, 2, 3]))


# Complete the code, so it works as expected.

# Output:
# [2, 3, 4]
