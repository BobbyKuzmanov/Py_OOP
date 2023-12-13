from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        return end - start

    return wrapper


# Test Code
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))

# Import the time module. Create a decorator called exec_time. It should calculate how much time a function needs to
# be executed. See the examples for more clarification.

# Output:
# 0.8342537879943848
