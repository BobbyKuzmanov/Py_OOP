def even_parameters(func):
    def wrapper(*args):
        if any(not isinstance(el, int) or el % 2 != 0 for el in args):
            return "Please use only even numbers!"
        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

# Create a decorator function called even_parameters. It should check if all parameters
# passed to a function are even numbers and only then execute the function and return the result.
# Otherwise, don't execute the function and return "Please use only even numbers!"

# Output:
# 6
# Please use only even numbers!
