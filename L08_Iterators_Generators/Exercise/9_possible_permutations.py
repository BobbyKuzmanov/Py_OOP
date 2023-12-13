def possible_permutations(numbers):
    if len(numbers) == 0:
        yield []
    else:
        for i in range(len(numbers)):
            element = numbers[i]
            remaining_elements = numbers[:i] + numbers[i + 1 :]
            for permutation in possible_permutations(remaining_elements):
                yield [element] + permutation


[print(n) for n in possible_permutations([1, 2, 3])]

# Create a generator function called possible_permutations() which should receive a
# list and return lists with all possible permutations between its elements.

# Output:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
