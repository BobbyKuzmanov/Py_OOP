def squares(n):
    current = 1
    while current <= n:
        yield current * current
        current += 1


print(list(squares(5)))

# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).
