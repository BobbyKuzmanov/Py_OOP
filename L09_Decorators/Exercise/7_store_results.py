class store_results:
    def __init__(self, func):  # reference to the function
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            result = self.func(*args, **kwargs)
            file.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")
            return result


# Test Code:
@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)

# Create a class called store_results. It should be used as a decorator and store information about the executed
# functions in a file called results.txt in the format: "Function {func_name} was called. Result: {func_result}"

# Output:
# Function 'add' was called. Result: 4
# Function 'mult' was called. Result: 24
