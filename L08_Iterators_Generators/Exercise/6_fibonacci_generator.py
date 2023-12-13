def fibonacci():
    curr_num, next_num = 0, 1
    while True:
        yield curr_num
        curr_num, next_num = next_num, curr_num + next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))

# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
# The first two numbers in the sequence are always 0 and 1.
# Each following Fibonacci number is created by the sum of the current number with the previous one.
