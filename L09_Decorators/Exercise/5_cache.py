def cache(func):  # call the function
    def wrapper(n):
        if not wrapper.log.get(n):  # check if the n is not in the dictionary
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    wrapper.log = {}  # create a dictionary
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Test code
fibonacci(3)
print(fibonacci.log)

# Create a decorator called cache. It should store all the returned values of the
# recursive function fibonacci. You are provided with this code:
# You need to create a dictionary called log that will store all the n's (keys) and the returned
# results (values) and attach that dictionary to the fibonacci function as a variable called log,
# so when you call it, it returns that dictionary.
