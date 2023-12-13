def solution():
    def integers():
        i = 1
        while True:
            yield i  # save current value
            i += 1  # increase current value

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]
        # result = []
        # for _ in range(n):
        #     result.append(next(seq))
        # return result

    return take, halves, integers


# Test code
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
print()
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

# Implement the three generator functions:
#     • integers() - generates an infinite amount of integers (starting from 1)
#     • halves() - generates the halves of those integers (each integer / 2)
#     • take(n, seq) - takes the first n halves of those integers
#
# Output:
# [0.5, 1.0, 1.5, 2.0, 2.5]
